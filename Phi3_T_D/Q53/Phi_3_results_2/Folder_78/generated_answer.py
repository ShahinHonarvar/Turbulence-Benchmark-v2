def expand_around_center(s, l, r):
    palindromes = set()
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        if r - l + 1 >= 96:
            palindromes.add(s[l:r + 1])
        l -= 1
        r += 1
    return palindromes

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        palindromes.update(expand_around_center(s, i, i))
        palindromes.update(expand_around_center(s, i, i + 1))
    return palindromes