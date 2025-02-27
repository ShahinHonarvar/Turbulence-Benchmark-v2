def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    result = set()
    text_lower = text.lower()
    for i in range(len(text_lower) - 86):
        substr = text_lower[i:i + 87]
        if is_palindrome(substr):
            result.add(substr)
    return result