from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, plaintext: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        plaintext = plaintext.upper()
        encrypt_text = []
        for i in plaintext:
            letter_index = self.alphabet.index(i)
            cipher = (letter_index + key) % alphabet_len
            cipher_text = self.alphabet(cipher)
            encrypt_text.append(cipher_text)
        return "".join(encrypt_text)

    def decrypt_text(self, ciphertext: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        ciphertext = ciphertext.upper()
        decrypt_text = []
        for i in ciphertext:
            letter_index = self.alphabet.index(i)
            plaintext = (letter_index - key) % alphabet_len
            plain_text = self.alphabet(plaintext)
            decrypt_text.append(plain_text)
        return "".join(decrypt_text)