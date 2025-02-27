import re

def palindrome_of_length_n(s):
    regex = re.compile('[a-zA-Z]{' + str(n) + '}')
    results = set()
    for match in regex.finditer(s):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            results.add(palindrome)
    return results