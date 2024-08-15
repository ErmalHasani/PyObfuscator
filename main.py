import argparse  # Module for parsing command-line arguments
import ast  # Module for Abstract Syntax Tree (AST) manipulation
import base64  # Module for encoding/decoding in Base64
import os  # Module for interacting with the operating system
import sys  # Module for system-specific parameters and functions

# Define ANSI escape codes for terminal text colors
PURPLE = "\033[95m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Define the ASCII banner with colors
banner = f"""\
{PURPLE}
            ▒█████   ▄▄▄▄     █████▒█    ██   ██████  ▄████▄   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███
            ▒██▒  ██▒▓█████▄ ▓██   ▒ ██  ▓██▒▒██    ▒ ▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
            ▒██░  ██▒▒██▒ ▄██▒████ ░▓██  ▒██░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
            ▒██   ██░▒██░█▀  ░▓█▒  ░▓▓█  ░██░  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄
            ░ ████▓▒░░▓█  ▀█▓░▒█░   ▒▒█████▓ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
            ░ ▒░▒░▒░ ░▒▓███▀▒ ▒ ░   ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
            ░ ▒ ▒░ ▒░▒   ░  ░     ░░▒░ ░ ░ ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
            ░ ░ ░ ▒   ░    ░  ░ ░    ░░░ ░ ░ ░  ░  ░  ░          ░   ▒    ░      ░ ░ ░ ▒    ░░   ░
                ░ ░   ░                ░           ░  ░ ░            ░  ░            ░ ░     ░
                        ░                          ░

                                    {BLUE}github profile github.com/ErmalHasani{RESET}
"""

# Print the banner to the terminal
print(banner)

class Obfuscator:
    def __init__(self):
        self.name_map = {}  # Dictionary to map original names to obfuscated names
        self.name_counter = 0  # Counter for generating unique names

    def generate_random_name(self) -> str:
        """Generate a unique random name."""
        self.name_counter += 1
        return f'__obf_{self.name_counter:04d}__'

    def obfuscate_identifiers(self, code: str) -> str:
        """Obfuscate function and variable names."""
        tree = ast.parse(code)  # Parse the code into an AST

        # Replace function names with obfuscated names
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                new_name = self.generate_random_name()
                self.name_map[node.name] = new_name
                node.name = new_name

        # Replace variable names with obfuscated names
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if node.id in self.name_map:
                    node.id = self.name_map[node.id]

        return ast.unparse(tree)  # Convert the AST back to code

    def encode_strings(self, code: str) -> str:
        """Base64 encode string literals."""
        def b64_encode(s: str) -> str:
            return f'__builtins__.__import__("base64").b64decode(b"{base64.b64encode(s.encode()).decode()}").decode()'

        tree = ast.parse(code)  # Parse the code into an AST
        new_code = code

        # Replace string literals with Base64 encoded versions
        for node in ast.walk(tree):
            if isinstance(node, ast.Str):
                encoded_str = b64_encode(node.s)
                new_code = new_code.replace(repr(node.s), encoded_str)

        return new_code

    def obfuscate_code(self, code: str) -> str:
        """Perform obfuscation on the code."""
        code = self.obfuscate_identifiers(code)  # Obfuscate identifiers
        code = self.encode_strings(code)  # Encode string literals
        return code

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description='Obfuscate Python code',
        usage='%(prog)s -i INPUT_FILE [-o OUTPUT_FILE]'
    )
    parser.add_argument('-i', '--input', required=True, help='Input file to obfuscate')
    parser.add_argument('-o', '--output', help='Output file', default=None)

    # Override the default error handling
    def custom_error(message):
        print(f'Usage: main.py -i INPUT_FILE [-o OUTPUT_FILE]')
        sys.exit(1)

    parser.error = custom_error

    # Parse command-line arguments
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output if args.output else input_file + '.obf.py'

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f'Error: Input file \'{input_file}\' does not exist')
        return

    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()

    obfuscator = Obfuscator()  # Create an Obfuscator instance
    obfuscated_code = obfuscator.obfuscate_code(code)  # Obfuscate the code

    # Write the obfuscated code to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(obfuscated_code)

    print(f'Obfuscated code written to {output_file}')

if __name__ == "__main__":
    main()  # Execute the main function when the script is run
