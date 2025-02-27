def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 86 and i < 99 and char.isalpha() and (char.lower() not in 'aeiou'):
            vowels.append(char)
    return vowels