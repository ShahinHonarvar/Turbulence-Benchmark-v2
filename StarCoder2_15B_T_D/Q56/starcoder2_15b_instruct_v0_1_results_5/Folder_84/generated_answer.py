import re

def all_substring_of_size_n(s):
    n = 114
    pattern = re.compile('.{' + str(n) + '}\\\\b')
    return list(set(pattern.findall(s)))