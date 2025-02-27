def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 10 and i < 82 and (char > '$') and (char <= '@'):
            vowels.append(char)
    return vowels