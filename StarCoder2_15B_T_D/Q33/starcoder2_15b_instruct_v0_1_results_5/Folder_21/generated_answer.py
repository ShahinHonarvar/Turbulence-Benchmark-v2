def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 464 and i < 574 and char.isalpha() and (char.lower() > 'a') and (char.lower() <= 'g'):
            vowels.append(char)
    return vowels