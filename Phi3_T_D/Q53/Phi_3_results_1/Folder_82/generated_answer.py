def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    for i in range(len(s)):
        for j in range(i + 72, len(s)):
            substr = s[i:j + 1]
            if is_palindrome(substr):
                result.add(substr)
    return result