# Password Generator

This is a simple Python password generator that offers both Command-Line Interface (CLI) and Graphical User Interface (GUI) modes. It allows users to generate strong passwords with customizable lengths and character sets.

## Features

- **CLI Mode:** Users can generate passwords directly from the command line interface.
- **GUI Mode:** Users can generate passwords using a user-friendly graphical interface.
- **Customization:** Users can specify the length of the password and choose whether to include letters, numbers, and symbols.

## How to Use

### CLI Mode

1. Open your terminal.
2. Navigate to the directory containing the `password_generator.py` file.
3. Run the script using the command `python password_generator.py`.
4. Follow the prompts to specify the password length and character set preferences.
5. The generated password will be displayed in the terminal.

### GUI Mode

1. Make sure you have Python installed on your system.
2. Open your terminal.
3. Navigate to the directory containing the `password_generator.py` file.
4. Run the script using the command `python password_generator.py`.
5. A graphical window will open with options to specify the password length and character set preferences.
6. Click the "Generate Password" button to generate a password.
7. The generated password will be copied to your clipboard automatically, ready to be pasted wherever needed.

## Dependencies

- Python 3.x
- tkinter (for GUI)

## License
- This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- This password generator was inspired by the need for strong, random passwords in today's digital age. Special thanks to the Python community for their invaluable resources and support.

	- Beginner: The CLI mode provides a simple command-line interface for generating passwords.

	- Advanced: The GUI mode offers a more user-friendly interface for generating passwords, suitable for those who prefer graphical applications.

- This version includes identifiers for both beginner and advanced sections.

## How to Install Dependencies

If you don't have Python installed, you can download it from the [official website](https://www.python.org/downloads/).

For the GUI mode, tkinter is included with most Python installations by default. If you encounter any issues with tkinter, you may need to install it separately using your package manager or through Python's package installer, pip.

```bash
# Install tkinter on Ubuntu/Debian
sudo apt-get install python3-tk

# Install tkinter on Fedora
sudo dnf install python3-tkinter

# Install tkinter using pip
pip install tk
