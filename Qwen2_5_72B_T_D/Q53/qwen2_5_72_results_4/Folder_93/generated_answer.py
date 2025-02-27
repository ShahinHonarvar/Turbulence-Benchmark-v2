def palindrome_of_length_at_least_n(text):
    text = text.lower()

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    n = len(text)
    for i in range(n):
        for j in range(i + 90, n + 1):
            if is_palindrome(text[i:j]):
                result.add(text[i:j])
    return result