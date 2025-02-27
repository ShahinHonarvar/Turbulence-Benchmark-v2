from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = ''.join([c for c in s if c.isalpha()])
    count = Counter(letters)

    def can_form_palindrome(counter):
        odd_count = sum((1 for v in counter.values() if v % 2 != 0))
        return odd_count <= 1
    if not can_form_palindrome(count) or len(letters) < 6:
        return set()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes