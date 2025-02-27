def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def expand(center, left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            if right - left + 1 >= 47:
                yield s[left:right + 1]
            left, right = (left - 1, right + 1)
    result = set()
    for i in range(len(s)):
        for p in expand(i, i, i):
            result.add(p)
        for p in expand(i, i, i + 1):
            result.add(p)
    return result