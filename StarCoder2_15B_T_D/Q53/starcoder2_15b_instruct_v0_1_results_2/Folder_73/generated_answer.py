import re

def palindrome_of_length_at_least_n(string):
    regex = '[a-zA-Z]{' + str(94) + ',}'
    palindromes = set()
    for match in re.finditer(regex, string, flags=re.IGNORECASE):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes