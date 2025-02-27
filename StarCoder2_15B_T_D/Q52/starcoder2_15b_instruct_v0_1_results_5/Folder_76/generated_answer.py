def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    for i in range(len(s) - 256):
        for j in range(i + 257, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and substring.isalpha():
                result.add(substring)
    return result