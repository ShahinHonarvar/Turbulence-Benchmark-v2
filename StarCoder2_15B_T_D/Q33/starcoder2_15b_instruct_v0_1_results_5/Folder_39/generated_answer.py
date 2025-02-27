def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 32 and i < 97 and char.isalpha() and (char.lower() > 'q') and (char.lower() <= ']'):
            vowels.append(char)
    return vowels