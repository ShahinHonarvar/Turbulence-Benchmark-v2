def expand_around_center(s, l, r, is_odd):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        if r - l - 1 >= 14 - 1:
            yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s)):
        yield from expand_around_center(s, i, i, True)
        yield from expand_around_center(s, i, i + 1, False)
    return res