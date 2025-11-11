from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# ----- Symmetric Encryption (Fernet) -----
message = b"Hello, this is a secret message."

# Generate symmetric key
symmetric_key = Fernet.generate_key()
cipher_suite = Fernet(symmetric_key)

# Encrypt message
encrypted_symmetric = cipher_suite.encrypt(message)

# Decrypt message
decrypted_symmetric = cipher_suite.decrypt(encrypted_symmetric)

# ----- Asymmetric Encryption (RSA) -----
# Generate RSA key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Encrypt using public key
encrypted_asymmetric = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt using private key
decrypted_asymmetric = private_key.decrypt(
    encrypted_asymmetric,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Write keys and outputs to a text file
with open('keys_and_output.txt', 'w') as f:
    f.write("SYMMETRIC KEY:\n")
    f.write(symmetric_key.decode() + "\n\n")
    
    f.write("SYMMETRIC ENCRYPTED:\n")
    f.write(encrypted_symmetric.decode() + "\n\n")
    
    f.write("SYMMETRIC DECRYPTED:\n")
    f.write(decrypted_symmetric.decode() + "\n\n")
    
    f.write("PUBLIC KEY:\n")
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode() + "\n")
    
    f.write("PRIVATE KEY:\n")
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode() + "\n\n")
    
    f.write("ASYMMETRIC ENCRYPTED (bytes):\n")
    f.write(str(encrypted_asymmetric) + "\n\n")
    
    f.write("ASYMMETRIC DECRYPTED:\n")
    f.write(decrypted_asymmetric.decode() + "\n")

# Create README file
with open('README.txt', 'w') as f:
    f.write("This project demonstrates symmetric and asymmetric encryption using Python.\n\n")
    f.write("1. Symmetric Encryption:\n")
    f.write("- Uses a single shared key (Fernet/AES)\n")
    f.write("- The same key is used to encrypt and decrypt the message.\n\n")
    f.write("2. Asymmetric Encryption:\n")
    f.write("- Uses a public/private key pair (RSA)\n")
    f.write("- Public key encrypts the message, private key decrypts it.\n\n")
    f.write("The file 'keys_and_output.txt' contains the keys used and the input/output results.\n")
