import re

def palindrome_of_length_n(string):
    pattern = re.compile('^(.)(?i)\\1{422}(?i)(.)\\2$', re.DOTALL)
    palindromes = set()
    for match in pattern.finditer(string):
        palindromes.add(match.group(0))
    return palindromes