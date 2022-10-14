import argparse

from cryptography_util.file_encryptor import FileEncryptor

if __name__ == '__main__':
    """
    Encryption/Decryption utility

    Usage Examples:
        python encryption_utils.py -h
        python encryption_utils.py keygen
        python encryption_utils.py encrypt -f test.txt
        python encryption_utils.py encrypt -f test.txt -kf encryption.key
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("task", type=str, choices=["keygen", "encrypt", "decrypt"],
                    help="select the task to perform (key generation, encrypt, decrypt)")
    parser.add_argument("-f", "--filename", type=str, help="The path of the file to encrypt/decrypt. Needed if encrypting/decrypting")
    parser.add_argument("-kf", "--key_filename", type=str, help="The path of the file where the key is stored. Fallbacks to manual input if none is given")


    args = parser.parse_args()

    if args.task == "keygen":
        FileEncryptor().generate_key()
    else:
        if args.filename:
            if not args.key_filename:
                args.key_filename = ""
            encryptor = FileEncryptor()
            encryptor.load_key(args.key_filename)
            if args.task == "encrypt":
                print(f"Encrypted file: {encryptor.encrypt_file(args.filename)}")
            else:
                print(f"Decrypted file: {encryptor.decrypt_file(args.filename)}")    
        else:
            print("You shall provide a file to encrypt/decrypt")