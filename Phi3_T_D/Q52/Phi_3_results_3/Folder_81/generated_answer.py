def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    result = set()

    def check_palindrome(start, end):
        while start >= 0 and end < n and (s[start] == s[end]):
            start -= 1
            end += 1
        return s[start + 1:end]
    for i in range(n - 98):
        substr = check_palindrome(i, i + 98)
        if len(substr) == 99:
            result.add(substr)
    return result