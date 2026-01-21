# AES Encryption Tool

## Overview
This project is a user-friendly file encryption and decryption tool developed using AES-based symmetric encryption.

It allows users to securely protect files using a password through a menu-driven interface.

---

## Features
- Encrypt files using AES-based encryption
- Decrypt encrypted files using the same password
- Menu-driven user-friendly interface
- Supports file name or full file path
- Error handling for invalid input and wrong passwords

---

## Project Structure

```
task4_aes_encryption_tool/
│
├── crypto_tool.py
└── README.md
```

---

## How It Works
- User selects an option from the menu
- Password is converted into a cryptographic key using SHA-256
- Key is used for AES-based encryption
- Encrypted files are saved with `.enc` extension
- Same password is required for decryption

---

## Installation Requirements

This tool depends on the `cryptography` library.

### Install dependencies
```bash
pip3 install -r requirements.txt
```

Make sure the installation is done using the same Python version used to run the tool.

---

## How to Use

### Step 1: Run the tool
```bash
python3 crypto_tool.py
```

### Step 2: Choose an option
```
1 → Encrypt a file
2 → Decrypt a file
3 → Exit
```

### Step 3: Provide file input
- Enter **file name** if the file is in the same directory
- Or enter **full file path** if located elsewhere

Example:
```
test.txt
```
or
```
/Users/username/Documents/test.txt
```

---

## Corner Cases & Error Handling
- Incorrect password → decryption fails safely
- Missing file → user is notified
- Encrypted files must end with `.enc`

---

## Technologies Used
- Python
- cryptography library
- AES-based encryption
- SHA-256 key derivation

---

## Disclaimer
This tool is developed strictly for educational purposes as part of an internship task.
