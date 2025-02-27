import re

def palindrome_of_length_at_least_n(s: str) -> set:
    regex = '[A-Za-z]{' + str(32) + ',}'
    matches = re.findall(regex, s, flags=re.IGNORECASE)
    return set((m for m in matches if m == m[::-1]))