import re

def palindromes_of_specific_lengths(s):
    pattern = '[a-zA-Z]{' + str(min_length) + ',' + str(max_length) + '}'
    matches = re.findall(pattern, s[65:100])
    return set([m for m in matches if m == m[::-1]])