def return_vowels(string):
    vowels = []
    for i, c in enumerate(string[20:43]):
        if i > 5 and i <= ord('M') and (c in 'aeiou'):
            vowels.append(c)
    return vowels