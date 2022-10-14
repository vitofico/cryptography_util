from cryptography.fernet import Fernet

class FileEncryptor():
    def __init__(self) -> None:
        self.key = None
    
    @staticmethod
    def generate_key(output_filename: str = "encryption") -> None:
        """Handy static method to generate an encryption key if needed

        Args:
            output_filename (str, optional): Optinal filename to save the key. Defaults to "encryption.key".
        """
        # key generation
        key = Fernet.generate_key()
        
        # string the key in a file
        with open(f'{output_filename}.key', 'wb') as filekey:
            filekey.write(key)
        
        return key

    def load_key(self, key_filename: str = "") -> str:
        """Loads the encryption key. By default tries to load it from a file
           and as a secondary method asks the user to insert it

        Args:
            key_filename (str): the complete file path where the key is stored

        Returns:
            str: the encryption key
        """
        try:
            with open(key_filename, 'rb') as filekey:
                self.key = filekey.read()
        except OSError:
            print('Error accessing file. Switching to manual mode')
            self.key = input("Enter key:")
        else:
            return self.key



    def encrypt_file(self, file_to_encrypt: str) -> None:
        """Encrypts the given file using the loaded key. The resulting file is saved as encrypted_<filename>

        Args:
            file_to_encrypt (str): the complete path of the file to encrypt

        Returns:
            str: the encrypted filename
        """
        fernet = Fernet(self.key)
        
        # opening the original file to encrypt
        with open(file_to_encrypt, 'rb') as file:
            original = file.read()
            
        # encrypting the file
        encrypted = fernet.encrypt(original)
        
        # opening the file in write mode and
        # writing the encrypted data
        out_filename = f'encrypted_{file_to_encrypt}'
        with open(out_filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        return out_filename

    def decrypt_file(self, file_to_decrypt: str) -> None:
        """Decrypts the given file using the loaded key

        Args:
            file_to_decrypt (str): the complete path of the file to decrypt. The resulting file is saved as decrypted_<filename>
        
        Returns:
            str: the decrypted filename
        """
        # using the key
        fernet = Fernet(self.key)
        
        # opening the encrypted file
        with open(file_to_decrypt, 'rb') as enc_file:
            encrypted = enc_file.read()
        
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        
        # opening the file in write mode and
        # writing the decrypted data
        out_filename = f"decrypted_{file_to_decrypt}"
        
        with open(out_filename, 'wb') as dec_file:
            dec_file.write(decrypted)

        return out_filename