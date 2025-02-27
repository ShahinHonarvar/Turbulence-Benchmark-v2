import re

def all_substring_of_size_n(string):
    substrings = re.findall('.{32}', string)
    distinct_substrings = []
    for substring in substrings:
        if len(set(substring)) == 32:
            distinct_substrings.append(substring)
    return distinct_substrings