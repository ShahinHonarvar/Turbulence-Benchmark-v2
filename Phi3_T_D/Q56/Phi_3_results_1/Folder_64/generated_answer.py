import itertools

def all_substring_of_size_n(input_string):
    substrings = []
    charset = set()
    for i in range(len(input_string) - 7):
        substring = input_string[i:i + 8]
        if len(set(substring)) == len(substring):
            if substring not in substrings:
                substrings.append(substring)
    distinct_substrings = list(set(substrings))
    return distinct_substrings