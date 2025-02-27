import re

def palindromes_of_specific_lengths(string):
    substring = string[31:92]
    pattern = '[a-zA-Z]{' + str(50) + ',' + str(53) + '}'
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    palindromes = {p for p in palindromes if p == p[::-1]}
    return palindromes