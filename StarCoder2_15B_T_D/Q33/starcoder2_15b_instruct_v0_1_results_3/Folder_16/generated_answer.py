def return_vowels(string, c, d):
    vowels = []
    for i, char in enumerate(string):
        if i >= 133 and i < 306 and char.isalpha() and (char.lower() in 'aeiou') and (char > c) and (char <= d):
            vowels.append(char)
    return vowels