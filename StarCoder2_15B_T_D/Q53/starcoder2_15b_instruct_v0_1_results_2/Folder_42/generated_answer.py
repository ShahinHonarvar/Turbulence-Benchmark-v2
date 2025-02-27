import re

def palindrome_of_length_at_least_n(string):
    regex = re.compile('\\b[a-zA-Z]{44,}\\b')
    palindromes = set()
    for match in regex.findall(string):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes