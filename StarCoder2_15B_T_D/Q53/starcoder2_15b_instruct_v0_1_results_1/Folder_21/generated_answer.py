import re

def palindrome_of_length_at_least_n(s):
    """
    Finds all palindromes of length at least 112 in the given string's'.
    Each palindrome should only consist of English letters.
    """
    palindromes = re.findall('(?i)(\\w{112,})', s)
    return {p for p in palindromes if p == p[::-1]}