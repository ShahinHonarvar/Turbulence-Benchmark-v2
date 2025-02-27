def is_all_alpha(s):
    return all((c.isalpha() for c in s))

def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        if r - l + 1 >= 41:
            yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for p in expand_around_center(s, i, i):
            if is_all_alpha(p):
                palindromes.add(p)
        for p in expand_around_center(s, i, i + 1):
            if is_all_alpha(p):
                palindromes.add(p)
    return palindromes