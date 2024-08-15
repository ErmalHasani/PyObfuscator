# PyObfuscator

**PyObfuscator** is a Python tool for obfuscating Python code. It renames functions and variables with unique identifiers and encodes string literals using Base64 to enhance code security and make reverse-engineering more challenging.

## Features

- **Identifier Obfuscation:** Replaces function and variable names with unique, non-descriptive names.
- **String Encoding:** Encodes string literals using Base64 to obscure their content.
- **Command-Line Interface:** Provides a simple way to specify input and output files via command-line arguments.

## Installation

Ensure you have Python 3.x installed. There are no additional dependencies required.

## Recommended Python Versions

- **Python 3.6 and newer**: The script uses features like **f-strings** and the **ast.unparse()** method, which were introduced in Python 3.6 and Python 3.9 respectively. Python 3.6 and later versions will work, but for the best support and additional features, Python 3.9 or newer is recommended.

## Python Version Compatibility

1. **Python 3.6:**

- Supports **f-strings** and basic ast module functionality.

2. **Python 3.7**

- Adds improvements to the **ast** module and other features.

3. **Python 3.8**

- Further improvements and optimizations in the **ast** module.

4. **Python 3.9 and newer**

- Introduces **ast.unparse()**, which is used in your script. Python 3.9 and newer will ensure full compatibility and access to the latest features and improvements.

## Usage

1. **Obfuscate Code:**

   ```bash
   python main.py -i input_file.py -o output_file.py
   ```

- **-i** specifies the input file containing the code to obfuscate.
- **-o** specifies the output file for the obfuscated code. If not provided, the output file will default to **<input_file>.obf.py.**

2. **Example:**
   ```bash
   python main.py -i my_script.py -o my_script.obf.py
   ```
   This command will read my_script.py, obfuscate the code, and save the result to **my_script.obf.py**.

3. **Command-Line Options:**

- **-i, --input**: Path to the input Python file to obfuscate (required).
- **-o, --output**: Path to the output file for the obfuscated code (optional).

## Summary

For the best compatibility and to leverage the latest features, it's recommended to run the script on Python 3.9 or later. Python 3.6 and Python 3.7 will work but may not support all the latest improvements. Ensure that you test your script with the desired Python version to verify compatibility.

## Error Handling

- If the input file does not exist, an error message will be displayed.
- A custom error message will guide users on correct usage if invalid arguments are provided.

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.html) for details.






