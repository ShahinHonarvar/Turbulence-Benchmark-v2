from any possible arrangement of English letters in the given string that occur between indices 3

def palindromes_between_indices(string):
    """
    Returns a set of all palindromes of the length of at least 3 such that each palindrome is created
    and 4, both inclusive.
    """
    palindromes = set()
    letters = [c for c in string.lower() if c.isalpha()]
    for i in range(len(letters) - 1):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j]
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes