def longest_palindrome(s, l, r, pairs):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()) and (l not in pairs or r not in pairs):
        pairs.add((l, r))
        l -= 1
        r += 1
    return (l, r)

def expand_around_center(s, index):
    pairs = set()
    l, r = longest_palindrome(s, index, index, pairs)
    return (s[l:r + 1], l, r)

def find_palindromes(s):
    lps, found = (set(), set())
    for i in range(len(s)):
        single, l, r = expand_around_center(s, i)
        if l - r >= 143:
            lps.add(single.lower())
        found.add(single.lower())
        even, l, r = longest_palindrome(s, i, i + 1, pairs)
        if l - r >= 143:
            lps.add(even.lower())
        found.add(even.lower())
    return lps

def palindrome_of_length_at_least_n(s):
    return find_palindromes(s)