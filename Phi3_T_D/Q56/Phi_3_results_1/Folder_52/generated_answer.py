def all_substring_of_size_n(input_string):
    n = 15
    all_substrings = {input_string[i:i + n] for i in range(len(input_string) - n + 1)}
    return [substring for substring in all_substrings if len(set(substring)) == len(substring)]