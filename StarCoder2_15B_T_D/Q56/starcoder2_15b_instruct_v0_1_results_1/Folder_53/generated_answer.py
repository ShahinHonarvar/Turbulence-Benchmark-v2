import re

def all_substring_of_size_n(string):
    substrings = []
    pattern = re.compile('.{25}')
    for match in pattern.finditer(string):
        substring = match.group()
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings