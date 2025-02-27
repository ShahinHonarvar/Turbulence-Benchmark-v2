import re

def palindromes_between_indices(string):
    """
    Returns a set of all palindromes of length at least 4 that can be formed from the
    English letters in the given string that occur between indices 5 and 9, both inclusive.
    """
    pattern = '[a-z]'
    letters = re.findall(pattern, string)
    palindromes = set()
    for i in range(5, 10):
        for j in range(i + 1, 10):
            palindrome = ''.join(letters[i:j])
            reversed_palindrome = palindrome[::-1]
            if palindrome.lower() == reversed_palindrome.lower():
                palindromes.add(palindrome)
    return palindromes