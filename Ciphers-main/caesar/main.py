import string
import sys

alp_list = list(string.ascii_lowercase)

def compute_cipher(n):
    if n > 0:
        alp_list.insert(0, alp_list.pop(-1))
        compute_cipher(n - 1)

def encrypt_char(alphabet, cipher, ch):
    ch1 = ch.lower()
    dict_list = dict(zip(list(alphabet), cipher))

    if dict_list.get(ch1) is not None:
        if ch1 != ch:
            return dict_list.get(ch1).upper()
        else:
            return dict_list.get(ch)
    else:
        return ch

def encrypt_str(alphabet, cipher, ch):
    encrypted_text = ""
    for element in ch:
        encrypted_text += encrypt_char(alphabet, cipher, element)
    return encrypted_text

def decrypt_str(alphabet, cipher, s):
    return encrypt_str(cipher, alphabet, s)

def encrypt_file(filename, alphabet, n):
    compute_cipher(n)

    with open(filename, 'r') as file:
        text = file.read()

    encrypted_text = encrypt_str(alphabet, alp_list, text)
    print(encrypted_text)

def decrypt_file(filename, alphabet, n):
    compute_cipher(n)

    with open(filename, 'r') as file:
        text = file.read()

    decrypted_text = decrypt_str(alphabet, alp_list, text)
    print(decrypted_text)


mode = sys.argv[1]
key = int(sys.argv[3])
filename = sys.argv[2]
alphabet = string.ascii_lowercase

if mode == "-encrypt":
    encrypt_file(filename, alphabet, key)
elif mode == "-decrypt":
    decrypt_file(filename, alphabet, key)
else:
    print("Invalid mode. Use 'encrypt' or 'decrypt'.")
