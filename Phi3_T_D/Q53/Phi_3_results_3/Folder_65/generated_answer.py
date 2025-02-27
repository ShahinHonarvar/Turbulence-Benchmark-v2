def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        if r - l + 1 >= 15:
            yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    return set((word for i in range(len(s)) for word in expand_around_center(s, i, i) and expand_around_center(s, i, i + 1)))