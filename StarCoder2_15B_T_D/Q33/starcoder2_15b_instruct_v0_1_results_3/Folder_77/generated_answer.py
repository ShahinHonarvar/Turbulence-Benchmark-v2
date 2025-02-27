def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 837 and i < 975 and char.isalpha() and (char.lower() in 'aeiou') and (char > 'N') and (char <= 'W'):
            vowels.append(char)
    return vowels