def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        if r - l + 1 >= 36:
            yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    L, R = (0, 0)
    result_set = set()
    while L < len(s):
        for palindrome in expand_around_center(s, L, L):
            result_set.add(palindrome)
        L += 1
        for palindrome in expand_around_center(s, L, L + 1):
            result_set.add(palindrome)
        L += 1
    return result_set