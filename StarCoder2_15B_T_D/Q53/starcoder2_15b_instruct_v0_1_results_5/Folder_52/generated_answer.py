import re

def palindrome_of_length_at_least_n(string: str) -> set:
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    palindromes = set(re.findall(pattern, string, flags=re.IGNORECASE))
    return {p for p in palindromes if p == p[::-1]}