def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    res = set()

    def expand(left, right):
        while left >= 0 and right < n and (s[left] == s[right]):
            if right - left + 1 >= 43:
                res.add(s[left:right + 1])
            left -= 1
            right += 1
    for i in range(n - 1):
        expand(i, i)
        expand(i, i + 1)
    return res