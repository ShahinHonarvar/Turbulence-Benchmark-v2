from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:6])).lower()
    cnt = Counter(letters)
    odd_char = [c for c, v in cnt.items() if v % 2 != 0]
    if len(odd_char) > 1 or len(letters) < 5:
        return set()
    half = ''.join((c * (v // 2) for c, v in cnt.items()))
    palindromes = set()
    for p in permutations(half):
        half_palindrome = ''.join(p)
        full_palindrome = half_palindrome + (odd_char[0] if odd_char else '') + half_palindrome[::-1]
        palindromes.add(full_palindrome)
    return palindromes