from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    letters = set(s)
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            half = ''.join(perm[:length // 2])
            if length % 2 == 0:
                palindrome = half + half[::-1]
            else:
                palindrome = half + perm[length // 2] + half[::-1]
            palindromes.add(palindrome)
    return palindromes