def return_vowels(string):
    vowels = [char for char in string[328:455] if char.isalpha() and char > '<' and (char <= 'z')]
    return vowels