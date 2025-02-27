import re

def palindrome_of_length_at_least_n(s):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, s, flags=re.IGNORECASE)
    palindromes = []
    for match in matches:
        if match == match[::-1]:
            palindromes.append(match)
    return set(palindromes)