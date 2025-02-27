def return_vowels(text):
    vowels = []
    for i, c in enumerate(text):
        if i >= 43 and i < 70 and c.isalpha() and (c.lower() in 'aeiou') and (c > '*') and (c <= 'b'):
            vowels.append(c)
    return vowels