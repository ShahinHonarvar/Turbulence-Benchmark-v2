def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 770 and i < 852 and char.isalpha() and (char.lower() in 'aeiou') and (char > 'B') and (char <= 'i'):
            vowels.append(char)
    return vowels