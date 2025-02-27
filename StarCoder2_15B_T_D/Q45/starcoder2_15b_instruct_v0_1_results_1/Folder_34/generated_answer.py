import re

def palindromes_between_indices(s):
    """
    Returns the set of all palindromes of the length of at least 4 such that each
    palindrome is created from any possible arrangement of the English letters in the
    given string that occur between index 5 to index 7, both inclusive. If no such
    palindromes of the specified length can be created from the English letters of the
    given string that occur in the specified range, the function should return an empty
    set. The function should form each palindrome in a case-insensitive manner.
    """
    palindromes = set()
    letters = re.findall('[a-zA-Z]', s)
    for i in range(len(letters)):
        for j in range(i + 3, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes