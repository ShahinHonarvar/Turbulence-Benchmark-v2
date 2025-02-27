def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        yield (l, r)
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for l, r in expand_around_center(s, 0, 0):
        if r - l + 1 >= 67:
            valid_palindrome = ''.join([c for c in s[l:r + 1] if c.isalpha()])
            if valid_palindrome:
                palindromes.add(valid_palindrome)
    return palindromes