# File Integrity Checker

This project is developed as part of the CODTECH Cyber Security Internship.

## Objective
To ensure file integrity by calculating and comparing SHA-256 hash values.

## Description
The tool calculates the hash of a file and stores it securely.  
On subsequent executions, the tool compares the current hash with the stored hash to detect any unauthorized file modifications.

## Technologies Used
- Python
- hashlib
- os module

## How to Run
1. Navigate to the project directory
2. Run the script:
   ```bash
   python3 integrity_checker.py
