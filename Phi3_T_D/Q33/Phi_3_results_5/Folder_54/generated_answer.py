def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in text[23:85] if 'W' < ch <= 'v' and ch in vowels]