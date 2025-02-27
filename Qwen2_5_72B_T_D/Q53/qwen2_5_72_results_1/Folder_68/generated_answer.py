def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text_lower = text.lower()
    palindromes = set()
    for i in range(len(text_lower)):
        for j in range(i + 20, len(text_lower)):
            substr = text_lower[i:j + 1]
            if is_palindrome(substr) and len(substr) >= 21:
                palindromes.add(substr)
    return palindromes