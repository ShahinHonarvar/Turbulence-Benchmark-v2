def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        yield s[left:right + 1]
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        p1 = expand_around_center(s, i, i)
        p2 = expand_around_center(s, i, i + 1)
        palindromes.update(p1)
        palindromes.update(p2)
    return {p for p in palindromes if len(p) >= 56}