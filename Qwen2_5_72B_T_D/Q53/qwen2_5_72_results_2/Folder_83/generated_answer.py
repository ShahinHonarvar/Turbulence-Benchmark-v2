def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 60, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result