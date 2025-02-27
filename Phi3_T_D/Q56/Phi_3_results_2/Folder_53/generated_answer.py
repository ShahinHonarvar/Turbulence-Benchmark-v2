from itertools import combinations

def all_substring_of_size_n(input_string):
    unique_chars = set(input_string)
    possible_substrings = combinations(unique_chars, 25)
    substrings = [''.join(char_combination) for char_combination in possible_substrings]
    return substrings