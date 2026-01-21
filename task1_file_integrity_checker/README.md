# File Integrity Checker

## Overview
The File Integrity Checker is a Python-based security tool developed as part of the CODTECH Cyber Security Internship.
Its purpose is to detect unauthorized or accidental modifications in files by using cryptographic hash functions.

This tool helps ensure that a file remains unchanged over time by comparing its current hash value with a previously stored hash.

---

## How It Works

1. The program reads the target file in **binary mode**.
2. A **SHA-256 cryptographic hash** is generated using the file’s content.
3. If no previous hash exists:
   - The generated hash is stored in a file (`hash_store.txt`).
4. On subsequent runs:
   - The current hash is recalculated.
   - The stored hash is loaded.
   - Both hashes are compared.
5. If the hashes match:
   - The file has **not been modified**.
6. If the hashes differ:
   - The file has been **altered or tampered with**.

Even a single-character change in the file will result in a completely different hash.

---

## Why SHA-256?

- Produces a fixed-length, unique output
- Highly resistant to collisions
- Widely used in security systems
- Suitable for file integrity verification

---

## Project Structure

task1_file_integrity_checker/
│
├── integrity_checker.py # Main Python script
├── sample.txt # Sample file for integrity testing
├── hash_store.txt # Stores the original file hash
└── README.md # Documentation


---

## How to Use

### Step 1: Navigate to the project directory
```bash
cd task1_file_integrity_checker
python3 integrity_checker.py
