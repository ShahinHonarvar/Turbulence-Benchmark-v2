def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for length in range(97, len(s) - i + 1):
            substr = s[i:i + length]
            if is_palindrome(substr):
                result.add(substr)
    return result