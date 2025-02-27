from collections import defaultdict

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        yield (left, right)
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    n = len(s)
    for center in range(2 * n - 1):
        left = center // 2
        right = left + center % 2
        for l, r in expand_around_center(s, left, right):
            if r - l + 1 >= 30:
                palindromes.add(s[l:r + 1])
                break
    return palindromes