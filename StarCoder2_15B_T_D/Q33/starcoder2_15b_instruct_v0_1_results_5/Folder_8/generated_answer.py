def return_vowels(string):
    vowels = []
    for char in string[64:82]:
        if char.isalpha() and char.lower() > 'p' and (char.lower() <= 'z'):
            vowels.append(char)
    return vowels