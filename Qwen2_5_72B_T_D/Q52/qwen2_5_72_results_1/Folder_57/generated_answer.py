def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    length = 92
    result = set()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if substring.isalpha() and is_palindrome(substring):
            result.add(substring)
    return result