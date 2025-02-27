def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 641 and i < 872 and c.isalpha() and (c.lower() in 'aeiou') and (c > '>') and (c <= 'q'):
            vowels.append(c)
    return vowels