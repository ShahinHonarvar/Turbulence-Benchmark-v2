import re

def palindrome_of_length_at_least_n(s):
    pattern = re.compile('([a-zA-Z]{56,})(\\1)', re.IGNORECASE)
    matches = pattern.findall(s)
    return set((match[0].lower() for match in matches))