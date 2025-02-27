from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10]
    letters = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            if perm == perm[::-1]:
                palindrome = ''.join(perm)
                palindromes.add(palindrome)
    return palindromes