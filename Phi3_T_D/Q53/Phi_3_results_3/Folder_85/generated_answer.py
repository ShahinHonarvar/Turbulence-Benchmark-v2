def expand_around_center(s, left, right):
    length = right - left + 1
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        length += 2 if length > 85 else 0
        left -= 1
        right += 1
    return (s[left + 1:right], length) if length >= 85 else (None, 0)

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        pl, len_pl = expand_around_center(s, i, i)
        if pl:
            palindromes.add(pl)
        pr, len_pr = expand_around_center(s, i, i + 1)
        if pr is not None:
            palindromes.add(pr)
    return palindromes