from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()[0:5]
    s_set = set(s)
    half_length = (len(s_set) + 1) // 2
    words = [''.join(p) for r in range(half_length, 0, -1) for p in permutations(s_set, r)]
    palindromes = {''.join(w + w[::-1][1:]) for w in words}
    return {p for p in palindromes if is_palindrome(p)}