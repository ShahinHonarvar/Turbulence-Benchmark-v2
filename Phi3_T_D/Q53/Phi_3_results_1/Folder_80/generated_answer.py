def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for center in range(len(s)):
        for palindrome in expand_around_center(s, center, center):
            if len(palindrome) >= 30:
                palindromes.add(palindrome)
        for palindrome in expand_around_center(s, center, center + 1):
            if len(palindrome) >= 30:
                palindromes.add(palindrome)
    return palindromes