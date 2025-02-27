def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if 65 <= i < 70 and char.isalpha() and (char.lower() > '%') and (char.lower() <= 'g'):
            vowels.append(char)
    return vowels