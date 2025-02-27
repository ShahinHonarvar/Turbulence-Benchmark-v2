from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:9])).lower()
    if len(letters) < 6:
        return set()
    palindromes = set()
    count = Counter(letters)
    odd_char = [k for k, v in count.items() if v % 2 == 1]
    if len(odd_char) > 1:
        return set()
    half_len = (len(letters) - (1 if odd_char else 0)) // 2
    half_palindrome = ''.join((k * (v // 2) for k, v in count.items()))
    for p in set(permutations(half_palindrome, half_len)):
        p = ''.join(p)
        palindromes.add(p + (odd_char[0] if odd_char else '') + p[::-1])
    return {p for p in palindromes if len(p) >= 6}