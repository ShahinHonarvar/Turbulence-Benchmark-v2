import re

def all_substring_of_size_n(s):
    pattern = re.compile('.{144}')
    return list(set(pattern.findall(s)))