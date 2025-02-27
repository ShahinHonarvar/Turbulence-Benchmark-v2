from itertools import permutations

def palindromes_between_indices(string):
    """
    Returns the set of all palindromes of the length of at least 6 such that each palindrome is created from any possible arrangement
    of the English letters in the given string that occur between index 2 to index 9, both inclusive.
    """
    letters = [c for c in string[2:10] if c.isalpha()]
    palindromes = set()
    for permutation in permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes