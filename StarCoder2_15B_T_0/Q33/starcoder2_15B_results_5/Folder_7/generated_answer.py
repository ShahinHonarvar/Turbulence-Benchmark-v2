def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 202 and i < 872 and (c in 'aeiou') and (c > '3') and (c <= '>'):
            vowels.append(c)
    return vowels