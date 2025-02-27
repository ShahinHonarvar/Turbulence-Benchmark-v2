def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 202 and i < 872 and (char > '3') and (char <= '>'):
            vowels.append(char)
    return vowels