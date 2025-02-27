def return_vowels(input_string):
    spec_range = input_string[86:99]
    vowels = [ch for ch in spec_range if ch in 'aeiou']
    filtered_vowels = [ch for ch in vowels if 'e' < ch <= 'r' or ord('E') < ord(ch) <= ord('R')]
    return filtered_vowels