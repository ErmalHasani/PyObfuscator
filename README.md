# PyObfuscator

**PyObfuscator** is a Python tool for obfuscating Python code. It renames functions and variables with unique identifiers and encodes string literals using Base64 to enhance code security and make reverse-engineering more challenging.

## Features

- **Identifier Obfuscation:** Replaces function and variable names with unique, non-descriptive names.
- **String Encoding:** Encodes string literals using Base64 to obscure their content.
- **Command-Line Interface:** Provides a simple way to specify input and output files via command-line arguments.

## Installation

Ensure you have Python 3.x installed. There are no additional dependencies required.

## Usage

1. **Obfuscate Code:**

   ```bash
   python pyobfuscator.py -i input_file.py -o output_file.py
   ```

- **-i** specifies the input file containing the code to obfuscate.
- **-o** specifies the output file for the obfuscated code. If not provided, the output file will default to **<input_file>.obf.py.**

2. **Example:**
   ```bash
   python pyobfuscator.py -i my_script.py -o my_script.obf.py
   ```
   This command will read my_script.py, obfuscate the code, and save the result to **my_script.obf.py**.

3. **Command-Line Options:**

- **-i, --input**: Path to the input Python file to obfuscate (required).
- **-o, --output**: Path to the output file for the obfuscated code (optional).

## Error Handling

- If the input file does not exist, an error message will be displayed.
- A custom error message will guide users on correct usage if invalid arguments are provided.

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.html) for details.






