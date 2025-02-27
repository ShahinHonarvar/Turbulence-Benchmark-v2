def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 24 and i < 68 and char.isalpha() and (char in 'aeiou') and (char > 'f') and (char <= '|'):
            vowels.append(char)
    return vowels