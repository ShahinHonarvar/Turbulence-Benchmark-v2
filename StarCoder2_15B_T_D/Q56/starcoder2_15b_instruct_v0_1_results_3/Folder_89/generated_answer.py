import itertools

def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 37):
        substring = string[i:i + 38]
        if len(set(substring)) == 38:
            substrings.add(substring)
    return list(substrings)