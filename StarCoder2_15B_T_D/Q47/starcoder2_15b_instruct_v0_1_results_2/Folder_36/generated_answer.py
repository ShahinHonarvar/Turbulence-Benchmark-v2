import re

def palindromes_of_specific_lengths(text):
    pattern = re.compile('[a-zA-Z]{115,134}')
    matches = pattern.findall(text[124:284])
    palindromes = {match for match in matches if match == match[::-1]}
    return palindromes