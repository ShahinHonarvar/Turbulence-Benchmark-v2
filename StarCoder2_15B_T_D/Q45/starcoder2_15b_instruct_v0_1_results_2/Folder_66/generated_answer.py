import itertools

def palindromes_between_indices(string):
    """
    Returns a set of all palindromes of the length of at least 5 such that
    each palindrome is created from any possible arrangement of the English
    letters in the given string that occur between index 0 to index 5, both inclusive.
    """
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for combination in itertools.permutations(letters, 5):
        palindrome = ''.join(combination)
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    return palindromes