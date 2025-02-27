def return_vowels(text):
    vowels = [c for c in text[63:79] if c.isalpha() and c.lower() in 'aeiou' and (c > 'D') and (c <= 'y')]
    return vowels