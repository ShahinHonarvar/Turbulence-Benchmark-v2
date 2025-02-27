def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 34 and i < 69 and char.isalpha() and (char.lower() in 'aeiou') and (char > '_') and (char <= 'o'):
            vowels.append(char)
    return vowels