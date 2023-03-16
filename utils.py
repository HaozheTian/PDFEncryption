from cryptography.fernet import Fernet

def write_key(key_directory):
    """
    Generate key and save to a file
    """
    key = Fernet.generate_key()
    with open(key_directory, "wb") as key_file:
        key_file.write(key)

def load_key(key_directory):
    """
    Load key file
    """
    return open(key_directory, "rb").read()

def encrypt_file(file_directory, key, inplace=0):
    """
    encrypt a file
    """
    f = Fernet(key)
    # read file
    with open(file_directory, "rb") as file:
        file_data = file.read()
    file_data_encrypted = f.encrypt(file_data)
    # write encrypted file
    if inplace:
        with open(file_directory, "wb") as file:
            file.write(file_data_encrypted)
    else:
        with open(file_directory[:-4] + "_encrypted.pdf", "wb") as file:
            file.write(file_data_encrypted)

def decrypt_file(file_directory, key, inplace=0):
    """
    decrypt an encrypted file
    """
    f = Fernet(key)
    with open(file_directory, "rb") as file:
        file_data_encrypted = file.read()
    file_Data = f.decrypt(file_data_encrypted)
    if inplace:
        with open(file_directory, "wb") as file:
            file.write(file_Data)
    else:
        with open(file_directory[:-4] + "_decrypted.pdf", "wb") as file:
            file.write(file_Data)



# write_key("key.key")

# key = load_key("key.key")
# encrypt_file("momentus.pdf", key)
# decrypt_file("momentus.pdf", key)

