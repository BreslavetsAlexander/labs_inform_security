class CaesarsCipher:
    def __init__(self, file_path, shift):
        self.file_path = file_path
        self.shift = shift
        self.content = self.output = None

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf8') as f:
            self.content = ''.join([line for line in f])

    def encrypt_text(self):
        self.output = list(self.content)
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet += alphabet.lower()
        half_length = len(alphabet) // 2
        for i in range(len(self.output)):
            if self.output[i] in alphabet:
                index_in_alphabet = alphabet.index(self.output[i])
                new_letter_index = (index_in_alphabet + self.shift) % half_length
                if index_in_alphabet > half_length - 1:
                    new_letter_index += half_length
                self.output[i] = alphabet[new_letter_index]
        self.output = ''.join(self.output)

    def write_file(self):
        with open('./encrypted.txt', 'w', encoding='utf8') as f:
            f.write(self.output)


caesars_cipher = CaesarsCipher('./initial.txt', 15)
caesars_cipher.read_file()
caesars_cipher.encrypt_text()
caesars_cipher.write_file()
