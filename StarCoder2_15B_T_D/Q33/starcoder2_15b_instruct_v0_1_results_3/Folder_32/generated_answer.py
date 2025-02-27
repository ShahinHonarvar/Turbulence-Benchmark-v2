def return_vowels(string):
    vowels = []
    for char in string:
        if char in VOWELS:
            vowels.append(char)
    return vowels