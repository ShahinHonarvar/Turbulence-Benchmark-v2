def find_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        l -= 1
        r += 1
    return (l + 1, r - 1)

def expand_around_center(s, center, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        left -= 1
        right += 1
    return (left + 1, right - 1)

def palindrome_of_length_at_least_n(s):
    n, result = (140, set())
    s = s.lower().replace(' ', '')
    for center in range(len(s)):
        left, right = expand_around_center(s, center, center, center)
        if right - left + 1 >= n:
            result.add(s[left:right + 1])
        left, right = expand_around_center(s, center, center - 1, center)
        if right - left + 1 >= n:
            result.add(s[left:right + 1])
    return result