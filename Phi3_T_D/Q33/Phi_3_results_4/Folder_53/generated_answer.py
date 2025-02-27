def return_vowels(s):
    return [char for char in s[27:57] if 'e' <= char <= 'w' and char.lower() not in 'eeoiou']