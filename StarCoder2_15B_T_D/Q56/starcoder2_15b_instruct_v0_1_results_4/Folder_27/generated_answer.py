import itertools

def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 57 + 1):
        substring = string[i:i + 57]
        if len(set(substring)) == 57:
            substrings.append(substring)
    return substrings