import itertools

def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(permutation).lower()
        if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes