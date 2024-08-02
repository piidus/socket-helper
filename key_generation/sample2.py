from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import hashlib
def generate_rsa_key_pair():
    """
    Generate an RSA key pair.

    This function generates a private and public RSA key pair using the cryptography library.
    The private key is generated with a public exponent of 65537 and a key size of 2048 bits.
    The public key is derived from the private key.

    Returns:
        private_key (rsa.RSAPrivateKey): The generated private RSA key.
        public_key (rsa.RSAPublicKey): The derived public RSA key.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    return private_key, public_key

def encrypt_message(message, public_key):
    """
    Encrypts a message using the provided public key.

    Args:
        message (str): The message to be encrypted.
        public_key (rsa.RSAPublicKey): The public key used for encryption.

    Returns:
        bytes: The encrypted message.

    Raises:
        TypeError: If the provided message is not a string.
        TypeError: If the provided public key is not an instance of rsa.RSAPublicKey.

    """
    encrypted_message = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashlib.sha256),
            algorithm=hashlib.sha256,
            label=None
        )
    )
    return encrypted_message

def decrypt_message(encrypted_message, private_key):
    """
    Decrypts an encrypted message using a private key.

    Args:
        encrypted_message (bytes): The encrypted message to be decrypted.
        private_key (rsa.RsaKey): The private key used for decryption.

    Returns:
        str: The original message, decoded from bytes to a string.

    Raises:
        ValueError: If the decryption fails or the message cannot be decoded.

    """
    original_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashlib.sha256),
            algorithm=hashlib.sha256,
            label=None
        )
    )
    return original_message.decode('utf-8')

# Example usage
private_key, public_key = generate_rsa_key_pair()

message = "Hello, world!"
encrypted_data = encrypt_message(message, public_key)
decrypted_data = decrypt_message(encrypted_data, private_key)

print("Original message:", message)
print("Encrypted message:", encrypted_data)
print("Decrypted message:", decrypted_data)
