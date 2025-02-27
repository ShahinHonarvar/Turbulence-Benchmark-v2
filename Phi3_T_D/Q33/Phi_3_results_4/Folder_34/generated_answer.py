def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in text[19:32] if char in vowels and ord(char) > 0 and (ord(char) <= 7)]
    return result