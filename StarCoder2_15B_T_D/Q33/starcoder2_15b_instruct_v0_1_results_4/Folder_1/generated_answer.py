def return_vowels(text):
    vowels = []
    for i, c in enumerate(text):
        if i >= 24 and i < 64 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'F') and (c <= 'h'):
            vowels.append(c)
    return vowels