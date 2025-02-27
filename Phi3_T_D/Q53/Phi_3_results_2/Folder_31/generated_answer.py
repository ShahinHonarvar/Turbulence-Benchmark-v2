def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        n = len(s)
        while left >= 0 and right < n and (s[left].lower() == s[right].lower()):
            if right - left + 1 >= 34:
                yield s[left:right + 1]
            left -= 1
            right += 1
    palindromes = set()
    for i in range(len(s)):
        yield from expand_around_center(i, i)
        yield from expand_around_center(i, i + 1)
    return palindromes