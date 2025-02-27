def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 4 and i < 8 and char.isalpha() and (char.lower() in 'aeiou') and (char > 'P') and (char <= 'r'):
            vowels.append(char)
    return vowels