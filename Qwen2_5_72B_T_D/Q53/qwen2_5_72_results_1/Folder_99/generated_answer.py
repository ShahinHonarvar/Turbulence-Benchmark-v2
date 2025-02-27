def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 114, len(s)):
            if is_palindrome(s[i:j + 1]):
                result.add(s[i:j + 1])
    return result