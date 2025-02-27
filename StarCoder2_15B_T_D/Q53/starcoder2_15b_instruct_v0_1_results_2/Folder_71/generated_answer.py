import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(87) + ',}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    palindromes = set((m for m in matches if m.lower() == m[::-1]))
    return palindromes