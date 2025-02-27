def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    result = set()
    for start in range(len(s)):
        for end in range(start + 9, len(s)):
            if all((c.isalpha() for c in s[start:end + 1])) and is_palindrome(s[start:end + 1]):
                result.add(s[start:end + 1])
    return result