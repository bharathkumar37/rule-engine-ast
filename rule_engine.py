class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # Can be 'operator' or 'operand'
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node
        self.value = value  # For 'operand' nodes (age, salary, etc.)

    def __repr__(self):
        return f"Node(type={self.node_type}, value={self.value})"

import ast

def parse_condition(cond_string):
    tree = ast.parse(cond_string, mode='eval')
    return convert_ast(tree.body)

def convert_ast(tree):
    if isinstance(tree, ast.BinOp):
        return Node(node_type='operator', left=convert_ast(tree.left),
                    right=convert_ast(tree.right), value=type(tree.op).__name__)
    elif isinstance(tree, ast.Compare):
        left_value = tree.left.id
        right_value = tree.comparators[0].n if isinstance(tree.comparators[0], ast.Constant) else tree.comparators[0].id
        operator = type(tree.ops[0]).__name__
        return Node(node_type='operand', value=f'{left_value} {operator} {right_value}')
    return None

def create_rule(rule_string):
    return parse_condition(rule_string)


def combine_rules(rules):
    combined_root = rules[0]
    
    for rule in rules[1:]:
        combined_root = Node(node_type='operator', left=combined_root, right=rule, value='OR')
    
    return combined_root

def evaluate_rule(ast_node, data):
    if ast_node.node_type == 'operand':
        left_operand, operator, right_operand = ast_node.value.split()
        left_value = data[left_operand]
        right_value = int(right_operand) if right_operand.isdigit() else data[right_operand]
        
        if operator == 'Gt':  # Greater than
            return left_value > right_value
        elif operator == 'Lt':  # Less than
            return left_value < right_value
        elif operator == 'Eq':  # Equal
            return left_value == right_value
    
    elif ast_node.node_type == 'operator':
        left_result = evaluate_rule(ast_node.left, data)
        right_result = evaluate_rule(ast_node.right, data)
        
        if ast_node.value == 'And':
            return left_result and right_result
        elif ast_node.value == 'Or':
            return left_result or right_result

    return False
