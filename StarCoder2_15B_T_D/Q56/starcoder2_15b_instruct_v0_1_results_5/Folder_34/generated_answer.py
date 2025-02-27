import itertools

def all_substring_of_size_n(input_string):
    if len(input_string) < 84:
        return []
    substrings = set()
    for i in range(len(input_string) - 83):
        substring = input_string[i:i + 84]
        if len(set(substring)) == 84:
            substrings.add(substring)
    return list(substrings)