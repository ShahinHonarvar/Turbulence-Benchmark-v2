def return_vowels(text):
    return [char for char in text[56:96] if char.isalpha() and char.lower() in 'aeiou' and (char > '&') and (char <= 'T')]