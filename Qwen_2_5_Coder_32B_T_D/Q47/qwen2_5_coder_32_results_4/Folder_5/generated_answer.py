import re

def palindromes_of_specific_lengths(s):
    s = s[63:71].lower()
    p = re.findall('[a-z]{4,5}', s)
    return {x for x in p if x == x[::-1]}