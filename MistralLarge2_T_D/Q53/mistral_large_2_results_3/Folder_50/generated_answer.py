def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    n = 91
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substr = s[i:j]
            if substr.isalpha() and is_palindrome(substr):
                result.add(substr)
    return result