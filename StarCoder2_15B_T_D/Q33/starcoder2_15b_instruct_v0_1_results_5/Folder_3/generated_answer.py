def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 50 and i < 77 and char.isalpha() and (char.lower() in 'aeiou') and (char > '#') and (char <= 'r'):
            vowels.append(char)
    return vowels