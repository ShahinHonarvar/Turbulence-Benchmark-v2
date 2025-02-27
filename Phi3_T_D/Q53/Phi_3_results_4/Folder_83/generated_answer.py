import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    pattern = '[a-zA-Z]{' + str(60) + ',}'
    matches = re.findall(pattern, s, flags=re.IGNORECASE)
    return {match.lower() for match in matches if is_palindrome(match.lower())}