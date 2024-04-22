# SHA256 Password Cracking

This Python script is a simple example of a password cracking tool that uses a brute-force approach to match a given SHA-256 hash against a list of common passwords.

## Disclaimer

The tools and scripts provided in this repository are made available for educational purposes only and are intended to be used for testing and protecting systems with the consent of the owners. The author does not take any responsibility for the misuse of these tools. It is the end user's responsibility to obey all applicable local, state, national, and international laws. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Under no circumstances should this tool be used for malicious purposes. The author of this tool advocates for the responsible and ethical use of security tools. Please use this tool responsibly and ethically, ensuring that you have proper authorization before engaging any system with the techniques demonstrated by this project.

## Features

- **Brute Force Hash Matching**: Attempts to match a given SHA-256 hash with a list of common passwords using a brute-force approach.
- **Password List Customization**: Utilizes a customizable password list to perform the hash matching.
- **Command-Line Interface**: Fully operable via command-line arguments, facilitating easy integration into other scripts or testing environments.
- **Progress Logging**: Leverages the pwn library's logging capabilities for real-time feedback on the cracking progress.

## Prerequisites

- **Operating System**: This script was tested on Kali Linux 2023.4. It should work on other Unix-like systems with appropriate modifications.
- **Python**: Version 3.7+
- **Python Libraries**:`pwn`: Primarily for logging and progress feedback.
- **Password List**: The script uses "10-million-password-list-top-100.txt" by default, ensure this file is downloaded and accessible.

## Installation

1. **Install Python**: Ensure Python 3.7+ is installed on your system. 
2. **Install Required Python Libraries**: Install the `pwn` library using pip:
    
    ```bash
    pip install pwntools
    ```
    
3. **Prepare Password List**: Ensure you have the password list file "10-million-password-list-top-100.txt" in the same directory as your script: https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
4. **Script Modifications**: Update the script accordingly to reflect your target word list if not using the default.

## Usage

To use the SHA256 Password Cracking tool:

```bash
python3 sha256-crack.py <your-sha256-hash>
```

- Replace `<your-sha256-hash>` with the actual hash you want to crack.

## How It Works

The script operates by iterating through a list of passwords, performing the following operations:

- **Reading Passwords**: Reads each password from a specified list, stripping newline characters and encoding appropriately.
- **Hashing Passwords**: Computes the SHA-256 hash for each password using the `sha256sumhex` function.
- **Matching Hash**: Compares the computed hash with the target hash provided as a command-line argument.
- **Logging Progress**: Uses the pwn library's log.progress to provide a visual indicator of the current state of the attempt, including success or failure feedback.
- **Successful Match**: If a password's hash matches the target hash, the script announces success and exits.
- **Exhausting Options**: If no match is found after exhausting the list, a failure message is logged.

## Output Example

```bash
python3 sha256-crack.py 11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1
Target Hash: 11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1
[+] Attempting to hack: 11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1!
    : Password hash found after 9 attempts! python hashes to 11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1!
```

## Contributing

If you have an idea for an improvement or if you're interested in collaborating, you are welcome to contribute. Please feel free to open an issue or submit a pull request.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
