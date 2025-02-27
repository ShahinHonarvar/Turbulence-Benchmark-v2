def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    n = 13
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring) and substring.isalpha():
            result.add(substring)
    return result