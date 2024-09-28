# XCryptor

You can securely encrypt files using military-grade encryption with the AES encryption algorithm.

It supports encryption and decryption of files in all formats (extensions).

Compatible with Windows, macOS, and Linux/UNIX operating systems.

## Usage

Command Line ONLY

### Set Target file path

```bash
--input, -i        Adds the path of the file to be encrypted/decrypted as an argument. (Required option)
--output, -o       Adds the path where the newly created encrypted/decrypted file will be saved. (Optional option)
```

### Encrypt and Decrypt Options

(If neither -e nor -d is specified, the -e option (encryption mode) is selected by default.)

```bash
--encrypt, -e      Encryption mode (Optional, default option)
--decrypt, -d      Decryption mode (Optional)
```

### Others

```bash
--remove, -r       Removes the original file after encryption/decryption is complete. (Optional)
--version, -v      Displays the program version information. (Standalone command)
--help, -h         Displays the usage information for the program. (Standalone command)
```

### Fast Encryption Execution (Minimum Required Options)
To encrypt a file, use the following command with the minimum required options:

```bash
XCryptor.py --input <path/to/input_file> --encrypt
```

### Fast Decryption Execution (Minimum Required Options)
To decrypt a file, use the following command with the minimum required options:

```bash
XCryptor.py --input <path/to/input_file> --decrypt
```

## Version history and Release here

[Release](https://github.com/XerosLab/XCryptor/releases)
