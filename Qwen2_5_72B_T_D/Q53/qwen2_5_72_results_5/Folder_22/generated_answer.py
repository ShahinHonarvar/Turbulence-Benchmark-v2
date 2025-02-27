def palindrome_of_length_at_least_n(text):
    text_lower = text.lower()
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(text_lower)):
        for j in range(i + 96, len(text_lower)):
            segment = text_lower[i:j + 1]
            if is_palindrome(segment) and segment.isalpha():
                palindromes.add(segment)
    return palindromes