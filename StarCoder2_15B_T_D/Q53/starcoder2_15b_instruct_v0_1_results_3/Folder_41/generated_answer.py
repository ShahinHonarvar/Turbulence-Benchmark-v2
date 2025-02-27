import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    pattern = '[a-z]{' + str(n) + ',}'
    palindromes = re.findall(pattern, string)
    palindromes = [p for p in palindromes if p == p[::-1]]
    return set(palindromes)