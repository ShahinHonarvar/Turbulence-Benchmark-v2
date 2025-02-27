def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 273 and i < 275 and (char > '+') and (char <= 'o'):
            vowels.append(char)
    return vowels