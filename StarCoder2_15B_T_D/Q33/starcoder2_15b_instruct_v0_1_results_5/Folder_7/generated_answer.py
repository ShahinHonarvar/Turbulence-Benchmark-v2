def return_vowels(string):
    return [c for i, c in enumerate(string) if i >= 202 and i < 872 and (c in 'aeiou') and (c > '3') and (c <= '>')]