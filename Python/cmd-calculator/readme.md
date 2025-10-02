# Command-Line Calculator

A small, easy-to-use command-line calculator written in Python. This script prompts the user for two numbers and a mathematical operation, then prints the result.

File: `command-line calculator.py`

## Features

- Add, subtract, multiply and divide two numbers
- Simple, interactive prompt-based UI (works in any terminal)
- Handles invalid number input and division-by-zero gracefully

## Requirements

- Python 3.6 or newer

No external libraries are required.

## How to run

1. Open a terminal and change to this directory:

```bash
cd Python/cmd-calculator
```

2. Run the script with Python 3:

```bash
python3 "command-line calculator.py"
```

If your system uses the `python` command for Python 3, you can run:

```bash
python "command-line calculator.py"
```

## Usage

When you run the script it will ask for:

- The first number
- The second number
- An operation: `+`, `-`, `*`, or `/`

Example session:

```
Command-Line Calculator
Enter the 1st number: 12
Enter the 2nd number: 4
Enter operation (+, -, *, /): /

Result: 12.0 / 4.0 = 3.0
```

Error handling behavior:

- If a non-numeric value is entered for either number, the script prints an error message and exits.
- If division by zero is attempted, the script prints an error message and exits.
- If an unsupported operation is entered, the script prints an error message and exits.

## Example inputs and expected outputs

- Input: `5`, `3`, `+` → Output: `Result: 5.0 + 3.0 = 8.0`
- Input: `7`, `2`, `*` → Output: `Result: 7.0 * 2.0 = 14.0`
- Input: `9`, `0`, `/` → Output: `Error: Cannot divide by zero!`

## Contributing

Contributions are welcome. If you'd like to improve the calculator, consider:

- Adding support for more operations (exponent, modulus, etc.)
- Adding command-line flags (e.g., non-interactive mode, piping input)
- Adding a simple test suite

Please open a pull request with a short description of the change.

## License

This project follows the repository license. See the top-level `LICENSE` file for details.

## Notes

- The script is intentionally minimal and written for clarity and learning. It's a good starter project for beginners learning Python and basic I/O.

