def return_vowels(string):
    vowels = [char for char in string[11:61] if char.isalpha() and char.lower() in 'aeiou' and ('m' < char.lower() <= 'w')]
    return vowels