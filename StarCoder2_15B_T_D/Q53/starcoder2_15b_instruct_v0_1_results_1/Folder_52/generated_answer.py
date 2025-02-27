import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    return set((m for m in matches if m == m[::-1]))