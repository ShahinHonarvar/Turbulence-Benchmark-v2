import itertools

def palindromes_between_indices(string):
    """
    Returns the set of all palindromes of the length of at least 4 such that
    each palindrome is created from any possible arrangement of the English
    letters in the given string that occur between index 2 to index 8, both inclusive.
    """
    letters = [c for c in string[2:9] if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes