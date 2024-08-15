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
