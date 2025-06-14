import unittest
from password_cracker import crack_sha1_hash

class TestPasswordCracker(unittest.TestCase):

    def test_unsalted_hashes(self):
        self.assertEqual(
            crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"),
            "password"
        )
        self.assertEqual(
            crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec"),
            "sammy123"
        )
        self.assertEqual(
            crack_sha1_hash("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e"),
            "abacab"
        )
        self.assertEqual(
            crack_sha1_hash("1234567890abcdef1234567890abcdef12345678"),
            "PASSWORD NOT IN DATABASE"
        )

    def test_salted_hashes(self):
        self.assertEqual(
            crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True),
            "superman"
        )
        self.assertEqual(
            crack_sha1_hash("da5a4e8cf89539e66097acd2f8af128acae2f8ae", use_salts=True),
            "q1w2e3r4t5"
        )
        self.assertEqual(
            crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", use_salts=True),
            "bubbles1"
        )
        self.assertEqual(
            crack_sha1_hash("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", use_salts=True),
            "PASSWORD NOT IN DATABASE"
        )

if __name__ == "__main__":
    unittest.main()
