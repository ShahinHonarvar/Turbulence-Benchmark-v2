from itertools import permutations
    from collections import Counter
    import string

def palindromes_between_indices(s):
    letters = s[:7].lower()
    valid_letters = [c for c in letters if c in string.ascii_lowercase]
    letter_counts = Counter(valid_letters)
    palindromes = set()
    for perm in permutations(valid_letters):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes