def is_palindrome(s):
    return s == s[::-1]

def expand_from_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        l, r = (l - 1, r + 1)
    return s[l + 1:r]

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        pl1 = expand_from_center(s, i, i)
        pl2 = expand_from_center(s, i, i + 1)
        for pl in [pl1, pl2]:
            if len(pl) >= 67 and is_palindrome(pl):
                palindromes.add(pl.lower())
    return palindromes