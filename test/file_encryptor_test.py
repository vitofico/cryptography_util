import unittest
import sys
import os

sys.path.insert(0, "../")

from cryptography_util.file_encryptor import FileEncryptor



class FileEncryptorTest(unittest.TestCase):
    DUMMY_ENCRYPTION_KEY = "OMMBGOliyxJODcrELZcSvbxKzuwKeVfNXq89s6NNPwU="
    DUMMY_FILE_CONTENT = "Don’t ever wrestle with a pig. You’ll both get dirty, but the pig will enjoy it."
    TEST_FILENAME = "test.txt"

    def test_generation(self):
        FileEncryptor().generate_key()
        file_exists = os.path.exists("encryption.key")
        self.assertTrue(file_exists)
        os.remove("encryption.key")
    
    def test_encryption_decryption(self):
        with open(self.TEST_FILENAME, 'w') as f:
            f.write(self.DUMMY_FILE_CONTENT)
        
        encryptor = FileEncryptor()
        encryptor.key = self.DUMMY_ENCRYPTION_KEY

        enc_filename = encryptor.encrypt_file(self.TEST_FILENAME)

        dec_filename = encryptor.decrypt_file(enc_filename)

        with open(dec_filename, 'r') as dec_file:
            decrypted = dec_file.read()
        
        self.assertEqual(decrypted, self.DUMMY_FILE_CONTENT)

        os.remove(enc_filename)
        os.remove(dec_filename)
        os.remove(self.TEST_FILENAME)
