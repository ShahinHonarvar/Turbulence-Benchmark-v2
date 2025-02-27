def palindrome_found(s, left, right, length):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        if right - left + 1 >= length:
            yield s[left:right + 1]
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s if c.isalpha()))
    return set((palindrome for length in range(7, len(s) + 1) for i in range(len(s)) for palindrome in palindrome_found(s, i, i, length)))