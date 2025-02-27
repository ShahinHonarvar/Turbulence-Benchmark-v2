def return_vowels(input_string):
    vowels_list = [ch for ch in input_string[20:58] if 'g' < ch <= 'a' and ch in 'aeiou']
    return vowels_list