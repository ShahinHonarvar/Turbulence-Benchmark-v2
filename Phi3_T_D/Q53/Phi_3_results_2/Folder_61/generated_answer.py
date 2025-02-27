def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        temp_set = set((pal for pal in expand_around_center(s, i, i)))
        temp_set |= set((pal for pal in expand_around_center(s, i, i + 1)))
        palindromes |= {pal for pal in temp_set if len(pal) >= 5}
    return palindromes