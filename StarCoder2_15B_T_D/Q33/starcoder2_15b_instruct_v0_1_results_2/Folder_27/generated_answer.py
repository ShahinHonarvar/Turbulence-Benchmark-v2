def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 29 and i < 31 and char.isalpha() and (char.lower() in 'aeiou'):
            vowels.append(char)
    return vowels