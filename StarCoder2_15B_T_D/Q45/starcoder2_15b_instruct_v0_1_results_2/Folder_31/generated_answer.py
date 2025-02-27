import itertools

def palindromes_between_indices(string):
    """
    Generate all possible arrangements of the English letters in the given string
    that occur between indices 1 and 8, both inclusive. Filter out the palindromes
    of length at least 6. Form each palindrome in a case-insensitive manner and
    return the set of all palindromes.
    """
    letters = [c for c in string if c.isalpha()]
    arrangements = itertools.combinations(letters, 8)
    palindromes = [''.join(arrangement) for arrangement in arrangements if len(arrangement) >= 6]
    case_insensitive_palindromes = {p.lower() for p in palindromes}
    return case_insensitive_palindromes