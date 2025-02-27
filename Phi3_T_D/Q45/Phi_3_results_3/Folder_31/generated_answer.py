from itertools import permutations
    from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[1:9].lower()
    counts = Counter(s)
    palindromes_set = set()
    for l in range(6, 9):
        if sum((1 for count in counts.values() if count < l // 2)) > l // 2:
            continue
        perms = set((''.join(p) for p in permutations(s, l)))
        palindromes_set.update(filter(is_palindrome, perms))
    return palindromes_set