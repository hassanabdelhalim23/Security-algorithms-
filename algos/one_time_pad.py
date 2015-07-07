def one_time_pad(text, key, enc_dec):
    if len(key) < len(text):
        return "The key length must be at least as long as the plain text length"
    key = list(key.replace(" ", "").lower())
    text = list(text.replace(" ", "").lower())
    for i, char in enumerate(text):

        if enc_dec == "enc":
            new_value = (ord(text[i]) - 97 + ord(key[i]) - 97) % 26
        else:
            new_value = ((ord(text[i]) - 97) - (ord(key[i]) - 97)) % 26

        #print ord(char) - 97, ord(key[i]) - 97, new_value
        text[i] = chr(new_value + 97)
    return ''.join(text)


#print one_time_pad("ahmadew","mostafa","enc")