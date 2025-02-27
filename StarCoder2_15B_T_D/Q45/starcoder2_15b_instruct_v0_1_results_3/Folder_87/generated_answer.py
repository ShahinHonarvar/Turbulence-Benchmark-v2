from itertools import permutations

def palindromes_between_indices(string):
    """
    Creates all possible palindromes of length at least 3 from the English letters in the given string
    that occur between index 3 and index 9, both inclusive.
    """
    letters = [c for c in string[3:10] if c.isalpha()]
    palindromes = set()
    for permutation in permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3 and palindrome.lower() == palindrome[::-1].lower():
            palindromes.add(palindrome)
    return palindromes