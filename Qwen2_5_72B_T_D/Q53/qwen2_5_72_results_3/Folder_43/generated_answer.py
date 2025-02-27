def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = ''.join(filter(str.isalpha, text.lower()))
    n = len(text)
    result = set()
    for i in range(n):
        for j in range(i + 48, n):
            if is_palindrome(text[i:j + 1]):
                result.add(text[i:j + 1])
    return result