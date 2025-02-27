def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 63 and i < 79 and char.isalpha() and (char.lower() in 'aeiou') and (char > 'D') and (char <= 'y'):
            vowels.append(char)
    return vowels