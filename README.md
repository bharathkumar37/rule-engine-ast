###Rule Engine with AST
This project is a simple rule engine implemented using an Abstract Syntax Tree (AST) to evaluate user eligibility based on attributes like age, department, income, and experience. The rule engine dynamically creates, combines, and evaluates rules.

##Features:
AST-based rule representation.
Dynamic rule creation, modification, and combination.
Evaluation of rules against user data.
Error handling and validation of rules.

##Prerequisites
Python 3.x installed on your system.
Git installed on your system (optional if you want to clone from GitHub).

###Installation
Step 1: Clone the repository
If you haven't already, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/bharathkumar37/rule-engine-ast.git
Navigate into the project directory:

bash
Copy code
cd rule-engine-ast
Step 2: Install Python
If you don't have Python installed, follow these steps:

Download the latest version of Python from the official website.
Run the installer and make sure to check the box that says "Add Python to PATH".
After installation, verify the installation by running:
bash
Copy code
python --version
or

bash
Copy code
python3 --version
This should return the version of Python installed (e.g., Python 3.x.x).

Running the Code
Step 1: Running the Rule Engine
Once Python is installed and the repository is cloned, you can run the main script:

bash
Copy code
python rule_engine.py
or

bash
Copy code
python3 rule_engine.py
This will execute the main rule engine logic. If there are no external dependencies, the program will create and evaluate rules based on the data.

Example Usage:
In rule_engine.py, you will find the logic to create rules, combine rules, and evaluate rules.

Creating a rule:

python
Copy code
rule = create_rule("age > 30 AND department == 'Sales'")
print(rule)
Combining rules:

python
Copy code
rule1 = create_rule("age > 30 AND department == 'Sales'")
rule2 = create_rule("salary > 50000")
combined_rule = combine_rules([rule1, rule2])
print(combined_rule)
Evaluating a rule:

python
Copy code
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
result = evaluate_rule(combined_rule, data)
print(result)  # Should return True or False based on evaluation
Running Test Cases
You can also run some test cases to validate that the rules are created, combined, and evaluated correctly. To do this:

Create a separate Python file (e.g., test_rule_engine.py) with the test cases.
Run the test cases with the following command:
bash
Copy code
python test_rule_engine.py
or

bash
Copy code
python3 test_rule_engine.py
Project Structure
rule_engine.py: Contains the main logic for creating, combining, and evaluating rules.
README.md: Contains instructions for running and testing the project.
Example Rules
Some sample rules that can be created and evaluated:

rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"


##How the Rule Engine Works:

Abstract Syntax Tree (AST): The rule engine uses an AST to represent rules. This allows for easy manipulation, evaluation, and combination of rules.
Creating Rules: The create_rule function takes a rule string as input and converts it into an AST.
Combining Rules: The combine_rules function takes multiple ASTs and combines them into a single AST.
Evaluating Rules: The evaluate_rule function takes a JSON representation of the AST and user data as input, and returns True or False based on whether the user satisfies the rule.

##Error Handling:
The system includes error handling for invalid rule strings and invalid user data.
Invalid comparisons or missing operators will raise a ValueError.
Advanced Features (Bonus)
Support for modifying existing rules using functions that allow changing operators, operand values, or sub-expressions.
Support for user-defined functions in rule expressions (for advanced users).


##License:
This project is licensed under the MIT License.
