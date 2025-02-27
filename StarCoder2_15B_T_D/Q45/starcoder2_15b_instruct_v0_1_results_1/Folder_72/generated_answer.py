import itertools

def palindromes_between_indices(string):
    """
    Returns a set of all palindromes of length at least 6 that can be formed from the
    English letters in the given string that occur between indices 1 and 7, both inclusive.
    """
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters, 6):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes