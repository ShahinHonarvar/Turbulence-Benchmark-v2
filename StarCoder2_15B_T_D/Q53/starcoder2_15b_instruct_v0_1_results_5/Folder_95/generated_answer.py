import re

def palindrome_of_length_at_least_n(string: str, n: int=35) -> set:
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    return set((match for match in matches if match == match[::-1]))