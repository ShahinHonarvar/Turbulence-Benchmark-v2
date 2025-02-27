import re

def palindromes_of_specific_lengths(string):
    palindromes = re.findall('(?i)([a-z]{26,31})', string[33:86])
    return set((palindrome for palindrome in palindromes if palindrome == palindrome[::-1]))