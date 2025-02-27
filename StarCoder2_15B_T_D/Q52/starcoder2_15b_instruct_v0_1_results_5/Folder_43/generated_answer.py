import re

def palindrome_of_length_n(string):
    palindromes = set()
    patterns = [f'(.{{51}})' for i in range(len(string) - 50)]
    for pattern in patterns:
        matches = re.findall(pattern, string, flags=re.IGNORECASE)
        for match in matches:
            if match == match[::-1] and match.isalpha():
                palindromes.add(match)
    return palindromes