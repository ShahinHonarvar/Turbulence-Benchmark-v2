def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    length = len(string)
    for i in range(length - 474 + 1):
        substring = string[i:i + 474]
        if is_palindrome(substring):
            result.add(substring)
    return result