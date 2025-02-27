from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    letters = s[:8].lower()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            half = ''.join(perm[:length // 2])
            if length % 2 == 0:
                palindrome = half + half[::-1]
            else:
                palindrome = half + perm[length // 2] + half[::-1]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result