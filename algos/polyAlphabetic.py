def encrypt(word, key):
    plain_text = list(word.upper().replace(' ', ''))
    key = key.upper().replace(' ', '')
    result = ""
    for i, char in enumerate(plain_text):
        sum_ = (char_pos(char) + char_pos(key[i % len(key)])) % 26
        final_result = sum_ + 65
        result += chr(final_result)
    return result

def decrypt(word, key):
    cipher_text = list(word.upper().replace(' ', ''))
    key = key.upper().replace(' ', '')
    result = ""
    for i, char in enumerate(cipher_text):
        sum_ = (char_pos(char) - char_pos(key[i % len(key)])) % 26
        final_result = sum_ + 65
        result += chr(final_result)
    return result

def char_pos(char):  # Returns the character position on a scale of (1 - 26)
    return ord(char) - 65

#print encrypt('WENEEDMORESNOW', 'ytiruces')
#print decrypt("UXVVYFQGPXAEIY", 'ytiruces')
#print encrypt("DCEF", "DE")
#print decrypt("GGHJ", "de")
#print encrypt("information engineering", "monarchy")
#print decrypt("UBSOIOHRUCAEEIPLQSEIEI", "monarchy")
