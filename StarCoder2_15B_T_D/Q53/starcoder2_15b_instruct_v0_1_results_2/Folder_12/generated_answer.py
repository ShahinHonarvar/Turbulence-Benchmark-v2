import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    lowercase_string = string.lower()
    match_pattern = re.compile('\\b[a-z]{51,}\\b')
    for match in match_pattern.findall(lowercase_string):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes