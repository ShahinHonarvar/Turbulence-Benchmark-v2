from itertools import permutations

def palindromes_between_indices(s):
    letters = sorted(s[:8].lower())
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            half = ''.join(perm[:r // 2])
            palindrome = half + half[::-1]
            if len(palindrome) <= r:
                palindromes.add(palindrome)
    return palindromes