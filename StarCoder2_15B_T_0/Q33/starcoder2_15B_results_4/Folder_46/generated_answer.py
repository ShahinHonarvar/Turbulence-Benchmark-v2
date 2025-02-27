def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 10 and i < 83 and (c in 'aeiou') and (c > '%') and (c <= 'e'):
            vowels.append(c)
    return vowels