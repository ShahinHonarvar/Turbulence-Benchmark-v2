def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 54 and i < 82 and ('a' <= c <= 'z') and (c in 'aeiou'):
            vowels.append(c)
    return vowels