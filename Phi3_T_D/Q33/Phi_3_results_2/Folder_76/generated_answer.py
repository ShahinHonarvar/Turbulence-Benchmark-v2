def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [letter for letter in input_string[495:837] if vowels[0] < letter <= 't' and letter in vowels]