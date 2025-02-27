def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        yield s[left:right + 1]
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s)):
        yield from expand_around_center(s_lower, i, i)
        yield from expand_around_center(s_lower, i, i + 1)
    return {p for p in palindromes if len(p) >= 69}