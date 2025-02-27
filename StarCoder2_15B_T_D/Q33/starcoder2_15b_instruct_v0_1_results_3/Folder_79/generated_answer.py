def return_vowels(string):
    vowels = []
    for i in range(74, 96):
        letter = string[i]
        if letter.isalpha() and letter.lower() in 'aeiou' and (letter > 'I') and (letter <= 'X'):
            vowels.append(letter)
    return vowels