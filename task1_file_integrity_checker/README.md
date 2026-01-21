# File Integrity Checker

## Overview
The File Integrity Checker is a Python-based security tool that detects unauthorized or accidental modifications to files.
It works by generating and comparing cryptographic hash values.

This tool demonstrates the concept of file integrity monitoring, which is widely used in cybersecurity to detect tampering.

---

## How It Works

1. The target file is read in binary mode.
2. A SHA-256 hash is generated from the file contents.
3. On first execution:
   - The hash is stored in `hash_store.txt`.
4. On subsequent executions:
   - The current hash is recalculated.
   - The stored hash is loaded.
   - Both hashes are compared.
5. If hashes differ, the file has been modified.

Even a single character change results in a completely different hash.

---

## Project Structure

```
task1_file_integrity_checker/
│
├── integrity_checker.py
├── sample.txt
├── hash_store.txt
└── README.md
```

---

## How to Use

### Step 1: Navigate to the directory
```bash
cd task1_file_integrity_checker
```

### Step 2: Run the script
```bash
python3 integrity_checker.py
```

### Step 3: Test integrity
- Run once to store the hash
- Modify `sample.txt`
- Run again to detect changes

---

## Example Output

**First Run**
```
Hash stored for the first time.
```

**After Modification**
```
WARNING: File has been modified!
```

---

## Corner Cases & Notes
- If `hash_store.txt` is deleted, the hash will be regenerated.
- The file must exist in the same directory unless the script is modified.
- Binary mode is required for correct hashing of non-text files.

---

## Technologies Used
- Python
- hashlib
- os module
