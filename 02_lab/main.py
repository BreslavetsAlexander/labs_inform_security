import random


class SimpleSubstitutionCipher:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, file_path):
        self.file_path = file_path
        self.key = self.__generate_key()
        self.content = self.encrypted_text = self.decrypted_text = None
        print(self.key)

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf8') as f:
            self.content = ''.join([line for line in f])

    def __generate_key(self):
        alphabet = SimpleSubstitutionCipher.alphabet
        alphabet_indexes = list(range(len(alphabet)))
        random.shuffle(alphabet_indexes)
        return ''.join([alphabet[i] for i in alphabet_indexes])

    def __helper(self, action='encrypt'):
        text = list(self.content)
        alphabet = SimpleSubstitutionCipher.alphabet
        alphabet += alphabet.lower()
        key = self.key
        if action == 'decrypt':
            text = list(self.encrypted_text)
            key, alphabet = alphabet, key + key.lower()
        half_length = len(alphabet) // 2
        for i in range(len(text)):
            if text[i] in alphabet:
                index_in_alphabet = alphabet.index(text[i])
                is_lower = False
                if index_in_alphabet > half_length - 1:
                    index_in_alphabet = index_in_alphabet % half_length
                    is_lower = True
                text[i] = key[index_in_alphabet]
                if is_lower:
                    text[i] = key[index_in_alphabet].lower()
        return ''.join(text)

    def encrypt_text(self):
        self.encrypted_text = self.__helper()

    def decrypt_text(self):
        self.decrypted_text = self.__helper('decrypt')
        print(self.decrypted_text == self.content)  # для проверки

    def write_file(self):
        with open('./encrypted.txt', 'w', encoding='utf8') as f:
            f.write(self.encrypted_text)


simple_substitution_cipher = SimpleSubstitutionCipher('./initial.txt')
simple_substitution_cipher.read_file()
simple_substitution_cipher.encrypt_text()
simple_substitution_cipher.decrypt_text()
simple_substitution_cipher.write_file()
