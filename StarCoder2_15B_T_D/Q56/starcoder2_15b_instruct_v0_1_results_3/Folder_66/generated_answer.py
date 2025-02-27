import itertools

def all_substring_of_size_n(text):
    substrings = set()
    for i in range(len(text) - 25):
        substring = text[i:i + 26]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)