def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 1 and i < 4 and (char.lower() > 'c') and (char.lower() <= 'i'):
            vowels.append(char)
    return vowels