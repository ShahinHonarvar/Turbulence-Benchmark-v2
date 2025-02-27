import itertools
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[:8] if c.isalpha()])
    counts = Counter(letters)
    half_len = 3
    half_palindrome = ''
    middle = ''
    for letter, count in counts.items():
        if count // 2 >= half_len - len(half_palindrome):
            half_palindrome += letter * (half_len - len(half_palindrome))
        if count % 2 == 1 and (not middle):
            middle = letter
    palindromes = set()
    if len(half_palindrome) == half_len:
        for perm in set(itertools.permutations(half_palindrome)):
            palindrome = ''.join(perm) + middle + ''.join(reversed(perm))
            palindromes.add(palindrome)
    return palindromes