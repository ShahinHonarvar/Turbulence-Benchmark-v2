from itertools import permutations

def palindromes_between_indices(s):
    subset = s[2:6].lower()
    chars = sorted(subset)
    palindromes = set()
    for r in range(3, len(chars) + 1):
        for perm in permutations(chars, r):
            half = ''.join(perm[:r // 2])
            palindrome = half + half[::-1]
            if len(palindrome) == r and palindrome.lower() in palindromes:
                continue
            palindromes.add(palindrome.lower())
    return palindromes