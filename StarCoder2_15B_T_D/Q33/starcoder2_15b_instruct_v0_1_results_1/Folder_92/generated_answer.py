def return_vowels(string: str) -> list:
    vowels = []
    for i, c in enumerate(string):
        if 3 <= i < 8 and c.isalpha() and (c.lower() in 'aeiou') and (c > ';') and (c <= 'D'):
            vowels.append(c)
    return vowels