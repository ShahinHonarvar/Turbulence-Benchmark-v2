def return_vowels(string):
    vowels = [char for char in string[27:57] if char.isalpha() and char > 'o' and (char <= 'w')]
    return vowels