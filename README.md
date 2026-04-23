# Hill Cipher

A simple command-line Hill Cipher encoder/decoder written in Python using NumPy.

## Overview

This project provides a small terminal application to:

- Encrypt plaintext into ciphertext using the Hill Cipher method
- Decrypt ciphertext back into plaintext
- Use matrix key sizes of **2x2**, **3x3**, or **4x4**

The main entry point is:

- `/home/runner/work/Hill-Cipher/Hill-Cipher/HillCipherFullApp.py`

## Features

- Interactive menu for encrypt/decrypt actions
- Automatic uppercase conversion for message and key input
- Supports alphabet-based encryption (`A-Z`)
- Removes spaces and numeric characters from message input
- Automatically pads message with `Z` when length is not compatible with selected key matrix size
- Validates key matrix invertibility before processing

## Project Structure

- `/home/runner/work/Hill-Cipher/Hill-Cipher/HillCipherFullApp.py`  
  Main menu application.
- `/home/runner/work/Hill-Cipher/Hill-Cipher/HillCipherEncrypt.py`  
  Encryption logic (`Encrypt()` function).
- `/home/runner/work/Hill-Cipher/Hill-Cipher/HillCipherDecrypt.py`  
  Decryption logic (`Decrypt()` function).
- `/home/runner/work/Hill-Cipher/Hill-Cipher/RunFullApp(ReadThisReference).txt`  
  External references used by the project.
- `/home/runner/work/Hill-Cipher/Hill-Cipher/Learn More/`  
  Image resources for learning/reference.

## Requirements

- Python 3.x
- NumPy

Install dependency:

```bash
pip install numpy
```

## How to Run

From the repository directory:

```bash
python HillCipherFullApp.py
```

Then choose from the menu:

1. Hill Cipher Encoder
2. Hill Cipher Decoder
3. Exit

## Usage Details

### Message Input Rules

- Message input is converted to uppercase.
- Spaces are ignored.
- Numeric characters are ignored.
- Characters outside the `A-Z` mapping are not officially supported.

### Key Rules

- Key length must be one of:
  - `4` characters (2x2 matrix)
  - `9` characters (3x3 matrix)
  - `16` characters (4x4 matrix)
- Key characters are converted from `A-Z` into numbers `0-25`.
- The key matrix must be invertible; otherwise, you must enter a new key.

### Padding Behavior

If message length is not divisible by matrix size, the app appends `Z` until valid.

## Example (Conceptual)

1. Start program and choose **Encoder**.
2. Enter plaintext, for example: `HELLO WORLD`.
3. Enter a key string of valid length (4, 9, or 16 chars).
4. Program outputs generated ciphertext.
5. Choose **Decoder** and use the same key to recover plaintext (including any `Z` padding that was added).

## Notes and Limitations

- This implementation is educational and terminal-based.
- It only works with the classical alphabet mapping (`A=0` to `Z=25`).
- Input sanitization is basic and may not handle all symbol edge cases.
- For decryption, some mathematically non-usable keys under modulo 26 may still be rejected at runtime.

## References

- Hill Cipher converter: https://www.dcode.fr/hill-cipher
- Hill Cipher explanation: https://www.geeksforgeeks.org/hill-cipher/
- NumPy matrix basics: https://www.programiz.com/python-programming/matrix

## Author

Application by **Bejjo**.
