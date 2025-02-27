import re

def palindrome_of_length_at_least_n(string):
    palindromes = re.findall('\\b[a-z]{70,}\\b', string.lower())
    return set((palindrome for palindrome in palindromes if palindrome == palindrome[::-1]))