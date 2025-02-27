import itertools

def palindromes_between_indices(string):
    string = string.upper()
    letters = [c for c in string[2:4] if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes