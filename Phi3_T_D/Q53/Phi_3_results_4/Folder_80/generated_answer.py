def palindrome_of_length_at_least_n(s):

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            if right - left >= 29:
                yield (left, right)
            left -= 1
            right += 1
    result = set()
    for i in range(len(s)):
        yield from expand_around_center(i, i)
        yield from expand_around_center(i, i + 1)
    for left, right in result:
        palindrome = s[left:right + 1]
        if palindrome.isalpha():
            result.add(palindrome.lower())
    return result