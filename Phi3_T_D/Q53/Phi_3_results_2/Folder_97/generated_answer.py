def palindrome_of_length_at_least_n(s):
    n = 138
    seen = set()
    s = s.lower()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                seen.add(substr)
    return seen