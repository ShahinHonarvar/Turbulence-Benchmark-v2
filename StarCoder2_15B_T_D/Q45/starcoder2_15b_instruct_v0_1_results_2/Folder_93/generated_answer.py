import itertools

def palindromes_between_indices(string):
    """
    Finds all palindromes of length at least 6 that can be formed from the
    English letters in the given string that occur between indices 2 and 7,
    both inclusive.
    """
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters[2:8]):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes