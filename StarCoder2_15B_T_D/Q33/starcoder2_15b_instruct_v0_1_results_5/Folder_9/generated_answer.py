def return_vowels(string):
    vowels = []
    for i, c in enumerate(string[13:35]):
        if i > 8 and i <= ord('F') and (c.lower() in 'aeiou'):
            vowels.append(c)
    return vowels