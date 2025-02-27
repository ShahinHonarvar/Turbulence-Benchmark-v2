def return_vowels(text):
    vowels = []
    for i, c in enumerate(text):
        if 40 <= i < 94 and c in 'AEIOU' and (c > '4') and (c <= 'H'):
            vowels.append(c)
    return vowels