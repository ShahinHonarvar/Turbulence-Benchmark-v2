def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 10 and i < 83 and (char > '%') and (char <= 'e'):
            vowels.append(char)
    return vowels