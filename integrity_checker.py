import hashlib
import os

def calculate_hash(filename):
    file = open(filename, "rb")
    content = file.read()
    file.close()
    return hashlib.sha256(content).hexdigest()

filename = "sample.txt"

current_hash = calculate_hash(filename)

if not os.path.exists("hash_store.txt"):
    store = open("hash_store.txt", "w")
    store.write(current_hash)
    store.close()
    print("Hash stored for the first time.")
else:
    store = open("hash_store.txt", "r")
    old_hash = store.read()
    store.close()

    if current_hash == old_hash:
        print("File is NOT modified.")
    else:
        print("WARNING: File has been modified!")
