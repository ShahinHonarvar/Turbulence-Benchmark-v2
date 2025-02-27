from itertools import combinations

def all_substring_of_size_n(input_string):
    substrings = list(set([''.join(substring) for i in range(len(input_string)) for j in range(i + 1, len(input_string) + 1) for substring in combinations(input_string[i:j], 57)]))
    return [s for s in substrings if len(set(s)) == len(s)]