import secrets
import hashlib

def generate_key_from_user_id(user_id):
  # Generate a strong random seed
  random_seed = secrets.token_bytes(32)

  # Combine with user ID
  combined_value = random_seed + user_id.encode('utf-8')

  # Derive key using SHA-256
  key = hashlib.sha256(combined_value).digest()

  return key
if __name__ == '__main__':
    # Example usage
    user_id = '123'
    key = generate_key_from_user_id(user_id)
    print(key)