def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 82 and i < 90 and char.isalpha() and (char.lower() in 'aeiou') and (char > 'T') and (char <= 'b'):
            vowels.append(char)
    return vowels