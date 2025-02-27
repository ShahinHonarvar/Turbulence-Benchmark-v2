import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters, 4):
        palindrome = ''.join(permutation)
        if palindrome[::1] == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes