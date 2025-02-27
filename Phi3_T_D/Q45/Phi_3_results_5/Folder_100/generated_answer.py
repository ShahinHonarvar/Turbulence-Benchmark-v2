from itertools import permutations

def palindromes_between_indices(s):
    eng_letters = [c.lower() for c in s[:6] if c.isalpha()]
    palindromes = set()
    for perm in permutations(eng_letters, 6):
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        palindromes.add(palindrome)
    return palindromes