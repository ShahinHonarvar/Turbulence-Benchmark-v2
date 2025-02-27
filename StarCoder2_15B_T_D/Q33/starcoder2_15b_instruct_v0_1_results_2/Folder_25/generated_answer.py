def return_vowels(input_string):
    substring = input_string[28:76]
    vowels = [char for char in substring if char.isalpha() and char.lower() in 'aeiou']
    filtered_vowels = list(filter(lambda x: x > '+' and x <= 'z', vowels))
    return filtered_vowels