def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 24 and i < 59 and char.isalpha() and (char.lower() in 'aeiou') and (char > 'N') and (char <= 'U'):
            vowels.append(char)
    return vowels