import re

def palindromes_of_specific_lengths(text):
    subtext = text[43:96]
    pattern = '[a-zA-Z]{18,47}'
    palindromes = set(re.findall(pattern, subtext, flags=re.IGNORECASE))
    return palindromes