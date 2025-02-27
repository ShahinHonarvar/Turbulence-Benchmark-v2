def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 529 and i < 828 and char.isalpha() and (char.lower() in 'aeiou') and (char > 'U') and (char <= 'l'):
            vowels.append(char)
    return vowels