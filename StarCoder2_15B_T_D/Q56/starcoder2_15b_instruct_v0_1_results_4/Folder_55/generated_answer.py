import re

def all_substring_of_size_n(string):
    pattern = '[a-zA-Z]{' + str(40) + '}'
    substrings = re.findall(pattern, string)
    distinct_substrings = list(set(substrings))
    return distinct_substrings