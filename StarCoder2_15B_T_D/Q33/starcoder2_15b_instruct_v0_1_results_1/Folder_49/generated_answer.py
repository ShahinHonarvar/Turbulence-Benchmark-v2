def return_vowels(string):
    vowels = []
    for i, char in enumerate(string):
        if i >= 10 and i < 97 and char.isalpha() and (char.lower() in 'aeiou') and (char > 'R') and (char <= 'b'):
            vowels.append(char)
    return vowels