def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 54 <= i < 82 and 'a' <= c <= 'z' and (c in 'aeiou'):
            vowels.append(c)
    return vowels