from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x.lower() in string.ascii_lowercase, s[7:10].lower()))
    letter_counts = Counter(letters)
    half = []
    for letter, count in letter_counts.items():
        half.extend([letter] * (count // 2))

    def is_palindrome(seq):
        return seq == seq[::-1]
    return {p[:(len(p) + 1) // 2] + p[len(p) // 2:] for p in set((''.join(p) for p in permutations(half))) if is_palindrome(p * 2) and len(p) * 2 >= 4}