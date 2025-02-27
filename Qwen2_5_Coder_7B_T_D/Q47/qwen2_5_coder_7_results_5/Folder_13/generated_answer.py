import re

def palindromes_of_specific_lengths(s):
    return set(re.findall('[a-zA-Z]{57,60}', s[13:96], re.IGNORECASE))