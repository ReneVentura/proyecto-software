from cryptography.fernet import Fernet
import pytest
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
        
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()
def encriptar_info(mensaje):
        
    write_key()
    message = mensaje.encode()
    key = load_key()
    f = Fernet(key)

    encrypted = f.encrypt(message)
    return encrypted




def desencriptar_info(m_encript):
    key = load_key()
    f = Fernet(key)
    decrypted_encrypted = f.decrypt(m_encript)
    return decrypted_encrypted


mensaje=encriptar_info("prueba")
print(mensaje)


print(desencriptar_info(mensaje))








def test_answer():
    encrt= encriptar_info("lol")

    assert desencriptar_info(encrt) == b'lol'
    

#decrypted_encrypted = f.decrypt(encrypted)
#print(decrypted_encrypted)