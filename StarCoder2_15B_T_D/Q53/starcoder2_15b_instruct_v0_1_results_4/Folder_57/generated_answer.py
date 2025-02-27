import re

def palindrome_of_length_at_least_n(string):
    """
    Returns the set of all palindromes of the length greater than or equal to 93 that
    exist in the given string. Each palindrome only consists of English letters. If no
    such palindromes exist in the given string, returns an empty set.
    """
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 92):
        window = string[i:i + 93]
        match = re.search('(.)(?=((\\1)\\3*)\\1)', window)
        if match:
            palindromes.add(match.group(0))
    return palindromes