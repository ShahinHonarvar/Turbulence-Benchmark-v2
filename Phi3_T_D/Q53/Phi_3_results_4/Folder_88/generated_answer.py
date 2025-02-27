def expand(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
    return s[left + 1:right]

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        palindromes.update(expand(s, i, i))
        palindromes.update(expand(s, i, i + 1))
    return {p for p in palindromes if len(p) >= 27}