import re

def all_substring_of_size_n(string):
    pattern = '.{47}'
    substrings = re.findall(pattern, string)
    distinct_substrings = []
    for substring in substrings:
        if len(set(substring)) == len(substring):
            distinct_substrings.append(substring)
    return distinct_substrings