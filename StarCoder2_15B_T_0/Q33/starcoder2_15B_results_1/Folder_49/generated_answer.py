def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 10 and i < 97 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'R') and (c <= 'b'):
            vowels.append(c)
    return vowels