def return_vowels(string):
    return [c for c in string[3:9] if c.isalpha() and c.lower() in 'aeiou' and (c > 's') and (c <= 'u')]