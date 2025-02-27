def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    if len(s) < 36:
        return set()
    palindromes = set()
    for i in range(len(s)):
        for j in expand_around_center(s, i, i):
            if len(j) >= 36:
                palindromes.add(j)
        for j in expand_around_center(s, i, i + 1):
            if len(j) >= 36:
                palindromes.add(j)
    return {p for p in palindromes if p.isalpha()}