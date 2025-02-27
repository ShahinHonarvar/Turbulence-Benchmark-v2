import itertools

def all_substring_of_size_n(string):
    substrings = [string[i:i + 61] for i in range(len(string) - 60)]
    return [substring for substring in substrings if len(set(substring)) == len(substring)]