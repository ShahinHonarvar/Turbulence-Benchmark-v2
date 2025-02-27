import re

def palindrome_of_length_at_least_n(text):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    palindromes = re.findall(pattern, text)
    result = set()
    for palindrome in palindromes:
        if palindrome == palindrome[::-1]:
            result.add(palindrome)
    return result