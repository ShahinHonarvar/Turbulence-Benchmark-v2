def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 82 and i < 90 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'T') and (c <= 'b'):
            vowels.append(c)
    return vowels