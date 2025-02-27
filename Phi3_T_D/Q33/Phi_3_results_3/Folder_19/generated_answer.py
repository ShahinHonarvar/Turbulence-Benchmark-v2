def return_vowels(text):
    return [char for char in text[51:77] if char in 'eiou' and ord('e') < ord(char) <= ord('=')]