def expand_around_center(s, l, r):
    n = len(s)
    while l >= 0 and r < n and (s[l].lower() == s[r].lower()):
        l, r = (l - 1, r + 1)
    return s[l + 1:r].lower()

def palindrome_of_length_at_least_n(s):
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 50, n):
            substr = expand_around_center(s, i, j)
            if len(substr) >= 51:
                palindromes.add(substr)
    return palindromes