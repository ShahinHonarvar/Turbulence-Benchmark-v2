def return_vowels(string):
    vowels = [char for char in string[64:82] if 'p' < char and char <= 'z' and (char in 'aeiou')]
    return vowels