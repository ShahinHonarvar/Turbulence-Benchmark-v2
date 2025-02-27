def palindrome_of_length_at_least_n(s):

    def expand(center, left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            yield s[left:right + 1]
            left -= 1
            right += 1
    result = set()
    for i in range(len(s)):
        for palindrome in list(expand(i, i - 1, i + 1)):
            if len(palindrome) >= 77:
                result.add(palindrome)
    return result