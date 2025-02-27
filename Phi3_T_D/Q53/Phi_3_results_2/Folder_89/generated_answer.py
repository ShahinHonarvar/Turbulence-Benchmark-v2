def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        if r - l + 1 >= 43:
            yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for palindrome in expand_around_center(s, i, i):
            palindromes.add(palindrome)
        for palindrome in expand_around_center(s, i, i + 1):
            palindromes.add(palindrome)
    return palindromes