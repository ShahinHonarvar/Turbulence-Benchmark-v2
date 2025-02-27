from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:5]]
    palindromes = set()
    for perm in permutations(letters, 4):
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        palindromes.add(palindrome if palindrome.isalpha() else '')
    return palindromes