def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 45 and i < 76 and char.isalpha() and (char.lower() > 'b') and (char.lower() <= 'z'):
            vowels.append(char)
    return vowels