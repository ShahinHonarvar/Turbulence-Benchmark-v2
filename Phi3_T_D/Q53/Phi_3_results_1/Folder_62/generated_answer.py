def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for pal in expand_around_center(s, i, i):
            if len(pal) >= 31:
                palindromes.add(pal.lower())
        for pal in expand_around_center(s, i, i + 1):
            if len(pal) >= 31:
                palindromes.add(pal.lower())
    return palindromes