def encrypt(plain_text, key):
    plain_text = list(plain_text.lower())
    for i, char in enumerate(plain_text):
        if (ord(char) - 96 + int(key)) == 27:  # Special check for the 'z'
            new_value = 32
        else:
            new_value = ((ord(char) - 96 + int(key)) % 27) + 96
        if ord(char) == 32:
            new_value = int(key) + 96
        plain_text[i] = chr(new_value)
    return ''.join(plain_text)

def decrypt(cipher_text, key):
    cipher_text = list(cipher_text.lower())
    for i, char in enumerate(cipher_text):
        if ord(char) - 96 - int(key) == 0:
            new_value = 32
        else:
            new_value = ((ord(char) - 96 - int(key)) % 27) + 96

        if ord(char) == 32:  # Special check for the space key
            new_value = ((ord(char) - 32 - int(key)) % 27) + 96
        #print 'P.T(', char, ') = (', ord(char) - 96, ' - ', key, ') mod 27 = ', new_value - 96, ' ==>', chr(new_value)
        cipher_text[i] = chr(new_value)
    return ''.join(cipher_text)

#print decrypt('nsktwrfyntsejslnsjjwnsl', 5)
#print encrypt('we need more snow', 2)

