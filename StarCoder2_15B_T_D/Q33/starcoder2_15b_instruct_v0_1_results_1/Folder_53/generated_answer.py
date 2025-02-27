def return_vowels(string):
    vowels = [letter for letter in string[27:57] if letter.isalpha() and letter.lower() > 'o' and (letter.lower() <= 'w')]
    return vowels