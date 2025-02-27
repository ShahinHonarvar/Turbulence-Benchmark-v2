def return_vowels(string):
    vowels = [char for char in string[71:88] if char.isalpha() and char.lower() in 'aeiou']
    return [char for char in vowels if char > '9' and char <= 'P']