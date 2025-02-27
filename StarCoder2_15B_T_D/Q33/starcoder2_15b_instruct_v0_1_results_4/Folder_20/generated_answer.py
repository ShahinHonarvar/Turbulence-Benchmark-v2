def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if c in 'aeiou' and 59 <= i < 61 and ('+' < c <= 'h'):
            vowels.append(c)
    return vowels