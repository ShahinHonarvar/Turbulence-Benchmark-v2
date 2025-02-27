import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters[4:6]):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes