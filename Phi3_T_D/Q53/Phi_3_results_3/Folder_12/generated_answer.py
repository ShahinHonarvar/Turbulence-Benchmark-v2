def expand_around_center(s, l, r):
    left = l
    right = r
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
    return s[left + 1:right].lower()

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s_lower = s.lower()
    for center in range(len(s)):
        palindrome_odd = expand_around_center(s_lower, center, center)
        if len(palindrome_odd) >= 51:
            palindromes.add(palindrome_odd)
        palindrome_even = ''
        if center + 1 < len(s):
            palindrome_even = expand_around_center(s_lower, center, center + 1)
            if len(palindrome_even) >= 51:
                palindromes.add(palindrome_even)
    return palindromes