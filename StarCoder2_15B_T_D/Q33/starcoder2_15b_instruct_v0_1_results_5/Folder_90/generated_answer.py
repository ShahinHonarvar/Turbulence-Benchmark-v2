def return_vowels(string):
    vowels = []
    for i, c in enumerate(string[142:145]):
        if c in 'aeiou' and c > '4' and (c <= 'o'):
            vowels.append(c)
    return vowels