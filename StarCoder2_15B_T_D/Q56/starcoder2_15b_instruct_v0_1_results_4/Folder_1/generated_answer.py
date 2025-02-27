def all_substring_of_size_n(input_string):
    substrings = [input_string[i:i + 24] for i in range(len(input_string) - 23)]
    distinct_substrings = [substring for substring in substrings if len(set(substring)) == 24]
    return distinct_substrings