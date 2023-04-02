# Third Party
from cryptography.fernet import Fernet

new_key = Fernet.generate_key()
decoded_key = new_key.decode()

print("***************")
print(f"Your new fernet key is: {decoded_key}")
print(
    f"Place it in your .env file. It's will be used to decrypt the messages on kafka topic."
)
print("***************")
