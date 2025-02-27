import re

def palindromes_between_indices(string):
    """
    Returns the set of all palindromes of length at least 3 that can be formed from any
    possible arrangement of the English letters in the given string that occur between indices
    0 and 5, both inclusive. If no such palindromes of the specified length can be formed,
    returns an empty set.
    """
    letters = re.findall('[a-z]', string.lower())
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes