import re

def all_substring_of_size_n(input_str):
    substrings = []
    pattern = '.{92}'
    for match in re.finditer(pattern, input_str):
        substring = match.group()
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings