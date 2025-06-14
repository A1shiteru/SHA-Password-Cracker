from password_cracker import crack_sha1_hash

# Without salts
print(crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"))  # Should return "password"

# With salts
print(crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True))  # Should return "superman"
# Example usage of the password cracker