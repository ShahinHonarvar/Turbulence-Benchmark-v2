def return_vowels(string):
    return [c for i, c in enumerate(string) if 32 <= i < 61 and c.isalpha() and (c.lower() in 'aeiou') and (c > '?') and (c <= 'P')]