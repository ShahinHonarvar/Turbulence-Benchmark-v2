def return_vowels(text):
    vowels = []
    for i, c in enumerate(text):
        if i >= 464 and i < 574 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'a') and (c <= 'g'):
            vowels.append(c)
    return vowels