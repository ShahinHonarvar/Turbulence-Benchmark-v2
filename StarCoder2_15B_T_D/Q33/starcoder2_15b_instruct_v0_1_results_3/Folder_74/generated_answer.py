def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 69 and i < 82 and ('a' <= c.lower() <= 'z') and (c.lower() in 'aeiou'):
            vowels.append(c)
    return vowels