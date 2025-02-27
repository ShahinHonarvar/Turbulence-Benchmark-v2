def palindrome_of_length_n(s):

    def expand(center, left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            yield s[left:right + 1]
            left -= 1
            right += 1
    result = set()
    for i in range(len(s)):
        for palindrome in expand(i, i, i):
            if len(palindrome) == 69:
                result.add(palindrome)
        for palindrome in expand(i, i, i + 1):
            if len(palindrome) == 69:
                result.add(palindrome)
    return result