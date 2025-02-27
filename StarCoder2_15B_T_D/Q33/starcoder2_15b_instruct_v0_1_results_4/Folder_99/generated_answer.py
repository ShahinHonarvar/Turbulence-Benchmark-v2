def return_vowels(text):
    vowels = []
    for i, c in enumerate(text):
        if 323 <= i < 526 and c.isalpha() and (c.lower() in 'aeiou'):
            vowels.append(c)
    return vowels