def return_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [ch for ch in input_string[43:70] if (ch > '*' and ch <= 'b') and ch in vowels]