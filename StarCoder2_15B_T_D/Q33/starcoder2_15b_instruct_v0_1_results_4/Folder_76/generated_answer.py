def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 495 and i < 837 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'B') and (c <= 't'):
            vowels.append(c)
    return vowels