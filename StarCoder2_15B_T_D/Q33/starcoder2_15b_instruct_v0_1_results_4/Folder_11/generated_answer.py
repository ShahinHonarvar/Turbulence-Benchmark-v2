def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 29 and i < 73 and c.isalpha() and (c.lower() in 'aeiou') and ('#' < c <= '('):
            vowels.append(c)
    return vowels