import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(95) + ',}'
    palindromes = re.findall(pattern, string)
    return set((palindrome for palindrome in palindromes if palindrome == palindrome[::-1]))