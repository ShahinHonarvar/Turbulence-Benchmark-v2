import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = re.compile('(?i)(\\b[a-z]{97,}\\b)', flags=re.I)
    matches = pattern.findall(string)
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes