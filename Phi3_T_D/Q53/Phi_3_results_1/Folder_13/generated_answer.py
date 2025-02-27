from collections import defaultdict

def expand_around_center(s, left, right, case_sensitive):
    if not case_sensitive:
        s = s.lower()
    while left >= 0 and right < len(s) and (s[left] == s[right]):
        left -= 1
        right += 1
    return s[left + 1:right]

def palindrome_of_length_at_least_n(s, case_sensitive=False):
    s = s.lower() if not case_sensitive else s
    result = set()
    for i in range(len(s)):
        pal_odd = expand_around_center(s, i, i + 1, case_sensitive)
        pal_even = expand_around_center(s, i, i, case_sensitive)
        if len(pal_odd) >= 52:
            result.add(pal_odd)
        if len(pal_even) >= 52:
            result.add(pal_even)
    return result