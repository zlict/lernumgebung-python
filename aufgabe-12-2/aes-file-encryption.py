# Install the needed library: pip install cryptography

# import required module
from cryptography.fernet import Fernet

## Encrypt File
def encrypt(original_file, encrypted_file, key):
    fernet = Fernet(key)

    with open(original_file, 'rb') as file:
        original_data = file.read()

    encripted_data = fernet.encrypt(original_data)

    with open(encrypted_file, 'wb') as enc_file:
        enc_file.write(encripted_data)

    print ("Original-Data\n---------\n" + str(original_data) + "\n")
    print ("Enc-Data\n---------\n" + str(encripted_data) + "\n")


## Decrypt File
def decrypt(encrypted_file, original_file, key):
    fernet = Fernet(key)

    with open(encrypted_file, 'rb') as enc_file:
        encripted_data = enc_file.read()

    original_data = fernet.decrypt(encripted_data)

    with open(original_file, 'wb') as file:
        file.write(original_data)

    print ("Enc-Data\n---------\n" + str(encripted_data) + "\n")
    print ("Original-Data\n---------\n" + str(original_data) + "\n")



# Generate Key
key = Fernet.generate_key()

# String the key in a file
with open('nba.csv.key', 'wb') as filekey:
   filekey.write(key)

# Encrypt & Decript the files
encrypt("nba.csv", "nba_enc.csv", key)
decrypt("nba_enc.csv", "nba_original.csv", key)
