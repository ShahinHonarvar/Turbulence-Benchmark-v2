def return_vowels(s):
    result = [c for c in s[1:9] if 'aAeEiIoOuU' > c > '?' and c <= 'k']
    return result