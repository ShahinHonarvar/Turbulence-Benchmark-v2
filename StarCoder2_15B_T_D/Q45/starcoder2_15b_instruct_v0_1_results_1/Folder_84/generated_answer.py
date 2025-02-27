import re

def palindromes_between_indices(text):
    """
    Creates all palindromes of length at least 3 from the English letters in the given string
    that occur between index 4 and index 9, both inclusive.
    """
    letters = re.findall('[a-z]', text.lower())
    palindromes = set()
    for i in range(4, 10):
        for j in range(i + 1, 10):
            palindrome = letters[i:j + 1] + letters[i:j:-1]
            palindromes.add(''.join(palindrome))
    return palindromes