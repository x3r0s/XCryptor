# XCryptor

You can securely encrypt files using military-grade encryption with the AES encryption algorithm.

It supports encryption and decryption of files in all formats (extensions).

Compatible with Windows, macOS, and Linux/UNIX operating systems.

## Usage

Command Line ONLY

### Command line options for XCryptor.py

```bash
XCryptor.py --input, -i        Adds the path of the file to be encrypted/decrypted as an argument. (Required option)
XCryptor.py --output, -o       Adds the path where the newly created encrypted/decrypted file will be saved. (Optional option)
XCryptor.py --encrypt, -e      Encryption mode (Optional, default option)
XCryptor.py --decrypt, -d      Decryption mode (Optional)
                    If neither -e nor -d is specified, the -e option (encryption mode) is selected by default.
XCryptor.py --remove, -r       Removes the original file after encryption/decryption is complete. (Optional)
XCryptor.py --version, -v      Displays the program version information. (Standalone command)
XCryptor.py --help, -h         Displays the usage information for the program. (Standalone command)
```

### Encryption Execution (Minimum Required Options)
To encrypt a file, use the following command with the minimum required options:

```bash
python XCryptor.py --input <path/to/input_file> --encrypt
```

### Decryption Execution (Minimum Required Options)
To decrypt a file, use the following command with the minimum required options:

```bash
python XCryptor.py --input <path/to/input_file> --decrypt
```

## Version history & Download

[Release](https://github.com/XerosLab/XCryptor/releases)
