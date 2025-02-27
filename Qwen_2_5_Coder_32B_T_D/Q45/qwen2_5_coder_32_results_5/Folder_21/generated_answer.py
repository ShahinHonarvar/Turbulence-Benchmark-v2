from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:9] if c.lower() in string.ascii_lowercase]
    letter_count = Counter(letters)
    half_len = 3
    mid = ''
    half_palindrome = ''
    for l, c in letter_count.items():
        if c % 2 == 1 and (not mid):
            mid = l
        half_palindrome += l * (c // 2)
    palindromes = set()
    for perm in permutations(half_palindrome):
        pal = ''.join(perm) + mid + ''.join(reversed(perm))
        palindromes.add(pal)
    return palindromes