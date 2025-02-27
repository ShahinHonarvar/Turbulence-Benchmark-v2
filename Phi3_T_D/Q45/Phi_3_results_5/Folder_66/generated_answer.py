from itertools import permutations
    from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[:6].lower()
    count_chars = Counter(s)
    valid_chars = ''.join([char * count for char, count in count_chars.items() if count >= 2])
    if len(valid_chars) < 5:
        return set()
    palindromes = set()
    for perm in permutations(valid_chars, 5):
        candidate = ''.join(perm[:2]) + 'x' + ''.join(reversed(perm[:2]))
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes