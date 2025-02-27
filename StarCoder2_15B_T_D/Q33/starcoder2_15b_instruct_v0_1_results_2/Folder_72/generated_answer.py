def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 37 and i < 57 and char.isalpha() and (char.lower() in 'aeiou') and (char > '*') and (char <= 'P'):
            vowels.append(char)
    return vowels