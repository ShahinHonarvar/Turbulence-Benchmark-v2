def return_vowels(string):
    vowels = [char for char in string[50:77] if char.isalpha() and char.lower() in 'aeiou' and (char > '#') and (char <= 'r')]
    return vowels