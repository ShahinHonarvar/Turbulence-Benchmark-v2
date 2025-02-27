from the English letters of the given string that occur in the specified range,

def palindromes_between_indices(string):
    """
    Given a string, return the set of all palindromes of the length of at least 5
    such that each palindrome is created from any possible arrangement of the
    English letters in the given string that occur between index 0 and index 6,
    both inclusive. If no such palindromes of the specified length can be created
    the function should return an empty set. The function should form each
    palindrome in a case-insensitive manner.
    """
    palindromes = set()
    letters = [c for c in string.lower() if c.isalpha()]
    for i in range(len(letters) - 4):
        for j in range(i + 5, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes