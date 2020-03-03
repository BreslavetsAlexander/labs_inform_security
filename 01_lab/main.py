class CaesarsCipher:
    def __init__(self, file_path, shift):
        self.file_path = file_path
        self.shift = shift
        self.content = self.encrypted_text = self.decrypted_text = None

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf8') as f:
            self.content = ''.join([line for line in f])

    def __helper(self, action='encrypt'):
        text = list(self.content)
        if action == 'decrypt':
            text = list(self.encrypted_text)
            self.shift = -self.shift
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet += alphabet.lower()
        half_length = len(alphabet) // 2
        for i in range(len(text)):
            if text[i] in alphabet:
                index_in_alphabet = alphabet.index(text[i])
                new_letter_index = (index_in_alphabet + self.shift) % half_length
                if index_in_alphabet > half_length - 1:
                    new_letter_index += half_length
                text[i] = alphabet[new_letter_index]
        return ''.join(text)

    def encrypt_text(self):
        self.encrypted_text = self.__helper()

    def decrypt_text(self):
        self.decrypted_text = self.__helper('decrypt')
        print(self.decrypted_text == self.content)  # для проверки

    def write_file(self):
        with open('./encrypted.txt', 'w', encoding='utf8') as f:
            f.write(self.encrypted_text)


caesars_cipher = CaesarsCipher('./initial.txt', int(input('Shift: ')))
caesars_cipher.read_file()
caesars_cipher.encrypt_text()
caesars_cipher.decrypt_text()
caesars_cipher.write_file()
