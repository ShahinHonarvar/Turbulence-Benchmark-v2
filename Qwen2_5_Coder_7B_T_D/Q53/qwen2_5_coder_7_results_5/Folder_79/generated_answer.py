def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    n = 17
    result = set()
    for i in range(len(text)):
        for j in range(i + n, len(text) + 1):
            substring = text[i:j]
            if is_palindrome(substring) and substring.isalpha():
                result.add(substring)
    return result