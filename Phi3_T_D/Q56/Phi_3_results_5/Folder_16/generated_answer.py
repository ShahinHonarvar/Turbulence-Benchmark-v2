def all_substring_of_size_n(input_string):
    substrings = {input_string[i:i + 124] for i in range(len(input_string) - 123)}
    distinct_substrings = [s for s in substrings if len(set(s)) == 124]
    return distinct_substrings