import re

def palindrome_of_length_n(text):
    """
    Finds all palindromes of length 38 in the given text. Each palindrome should only
    consist of English letters. If there are no palindromes, an empty set is returned.
    """
    substrings = re.findall('.{38}', text, flags=re.DOTALL)
    palindromes = set()
    for substring in substrings:
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes