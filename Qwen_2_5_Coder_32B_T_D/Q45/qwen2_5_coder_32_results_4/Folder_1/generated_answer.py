from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    char_count = Counter(s[4:8].lower())
    chars = ''.join((c * (count // 2) for c, count in char_count.items()))

    def is_palindrome(p):
        return p == p[::-1]
    palindromes = set()
    for perm in set(permutations(chars)):
        half = ''.join(perm)
        full = half + s[4:8].lower().count(half[0]) % 2 * half[0] + half[::-1]
        if len(full) >= 5 and is_palindrome(full):
            palindromes.add(full)
    return palindromes