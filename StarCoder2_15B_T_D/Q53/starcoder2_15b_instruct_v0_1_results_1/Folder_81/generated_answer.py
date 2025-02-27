import re

def palindrome_of_length_at_least_n(s):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, s, flags=re.IGNORECASE)
    return {m for m in matches if m == m[::-1] and len(m) >= 33}