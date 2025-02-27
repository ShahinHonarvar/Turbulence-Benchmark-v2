import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    range_len = 8
    s = s[:range_len]
    s = ''.join(filter(str.isalpha, s)).lower()
    letter_counts = {letter: s.count(letter) for letter in set(s)}
    palindromes = {s[:range_len // 2] + s[:range_len // 2][::-1] for s in itertools.permutations(s)}
    return {p for p in palindromes if len(p) >= 7 and is_palindrome(p) and (letter_counts == {c: p.count(c) for c in p})}