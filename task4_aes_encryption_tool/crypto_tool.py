from cryptography.fernet import Fernet
import base64
import hashlib
import os
print("📂 Current working directory:", os.getcwd())

def generate_key(password):
    return base64.urlsafe_b64encode(
        hashlib.sha256(password.encode()).digest()
    )

def encrypt_file():
    filename = input(
    "Enter file name OR full file path to encrypt (file must exist in this folder or provide full path): "
).strip()


    if not os.path.exists(filename):
        print("❌ File not found.")
        return

    password = input("Enter password: ")

    key = generate_key(password)
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print("✅ File encrypted successfully.")
    print("Encrypted file:", filename + ".enc")

def decrypt_file():
    filename = input(
    "Enter encrypted file name OR full file path (.enc): "
).strip()


    if not os.path.exists(filename):
        print("❌ File not found.")
        return

    password = input("Enter password: ")

    key = generate_key(password)
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception:
        print("❌ Incorrect password or corrupted file.")
        return

    original_file = filename.replace(".enc", "")

    with open(original_file, "wb") as file:
        file.write(decrypted_data)

    print("✅ File decrypted successfully.")
    print("Restored file:", original_file)

def main():
    while True:
        print("\n=== AES Encryption Tool ===")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            encrypt_file()
        elif choice == "2":
            decrypt_file()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
