import hashlib

def crack_sha1_hash(hash_to_crack, use_salts=False):
    with open("top-10000-passwords.txt", "r") as f:
        passwords = [line.strip() for line in f]

    salts = []
    if use_salts:
        with open("known-salts.txt", "r") as f:
            salts = [line.strip() for line in f]

    for password in passwords:
        if use_salts:
            for salt in salts:
                salted_variants = [
                    salt + password,
                    password + salt
                ]
                for variant in salted_variants:
                    hashed = hashlib.sha1(variant.encode()).hexdigest()
                    if hashed == hash_to_crack:
                        return password
        else:
            hashed = hashlib.sha1(password.encode()).hexdigest()
            if hashed == hash_to_crack:
                return password

    return "PASSWORD NOT IN DATABASE"
