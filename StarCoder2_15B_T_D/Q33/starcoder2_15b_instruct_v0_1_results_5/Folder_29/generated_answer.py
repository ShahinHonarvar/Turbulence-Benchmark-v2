def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i in range(19, 20) and c.isalpha() and (c.lower() in 'aeiou') and ('a' < c <= 'p'):
            vowels.append(c)
    return vowels