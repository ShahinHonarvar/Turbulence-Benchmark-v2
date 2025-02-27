def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 56 and i < 90 and char.isalpha() and (char.lower() in 'aeiou'):
            vowels.append(char)
    return vowels