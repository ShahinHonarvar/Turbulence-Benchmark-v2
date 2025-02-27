def return_vowels(text):
    return [char for char in text[45:76] if char in 'aeiou' and ord(char) > ord('b') and (ord(char) <= ord('z'))]