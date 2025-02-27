import re

def palindrome_of_length_n(string):
    pattern = re.compile('(?i)(?=(\\w{' + str(42) + '}))(?:\x02(?!$)|^(?<!^)\x02$)')
    palindromes = set()
    for match in pattern.finditer(string):
        palindrome = match.group(1).lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes