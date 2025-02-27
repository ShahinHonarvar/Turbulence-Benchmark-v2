from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = list(s)
    palindrome_set = set()
    for r in range(7, len(letters) + 1):
        for p in permutations(letters, r):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set