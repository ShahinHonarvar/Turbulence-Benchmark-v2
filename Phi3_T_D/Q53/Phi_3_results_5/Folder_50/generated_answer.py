def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            yield s[left:right + 1]
            left -= 1
            right += 1
    result = set()
    for i in range(len(s)):
        odd_pal = expand_around_center(i, i)
        even_pal = expand_around_center(i, i + 1)
        for p in odd_pal:
            if len(p) >= 91:
                result.add(p)
        for p in even_pal:
            if len(p) >= 91:
                result.add(p)
    return result