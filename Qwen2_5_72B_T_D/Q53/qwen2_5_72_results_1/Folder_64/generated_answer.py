def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    n = len(text)
    result = set()
    for i in range(n):
        for j in range(i + 9, n + 1):
            substring = text[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result