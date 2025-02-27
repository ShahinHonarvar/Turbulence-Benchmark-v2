import itertools

def palindromes_between_indices(string):
    letters = [c for c in string[1:8] if c.isalpha()]
    permutations = itertools.permutations(letters, len(letters))
    palindromes = set()
    for permutation in permutations:
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes