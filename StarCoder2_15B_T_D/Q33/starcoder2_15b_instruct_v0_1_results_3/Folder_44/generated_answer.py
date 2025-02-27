def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 46 and i < 49 and char.isalpha() and (char.lower() in 'aeiou') and (char > '[') and (char <= 'p'):
            vowels.append(char)
    return vowels