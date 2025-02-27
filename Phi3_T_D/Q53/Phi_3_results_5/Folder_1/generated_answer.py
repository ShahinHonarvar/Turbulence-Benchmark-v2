def palindrome_of_length_at_least_n(s):

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left].isalpha() and s[right].isalpha() and (s[left].lower() == s[right].lower()):
            yield s[left:right + 1]
            left -= 1
            right += 1
    result = set()
    for i in range(len(s)):
        for palindrome in expand_around_center(s, i, i):
            if len(palindrome) >= 29:
                result.add(palindrome)
        for palindrome in expand_around_center(s, i, i + 1):
            if len(palindrome) >= 29:
                result.add(palindrome)
    return result