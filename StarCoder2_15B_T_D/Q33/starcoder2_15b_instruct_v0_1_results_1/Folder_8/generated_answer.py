def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if 64 < i < 82 and char.isalpha() and (char.lower() > 'p') and (char.lower() <= 'z'):
            vowels.append(char)
    return vowels