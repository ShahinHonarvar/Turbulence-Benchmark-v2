def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 8 and i < 9 and char.isalpha() and (char.lower() in 'aeiou') and (char > 'Y') and (char <= 's'):
            vowels.append(char)
    return vowels