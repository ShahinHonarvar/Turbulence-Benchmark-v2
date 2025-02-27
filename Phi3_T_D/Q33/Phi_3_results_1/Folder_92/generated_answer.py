def return_vowels(input_string):
    result = [char for char in input_string[3:8] if char > ';' and char <= 'D']
    return [vowel for vowel in result if vowel in 'AEIOUaeiou']