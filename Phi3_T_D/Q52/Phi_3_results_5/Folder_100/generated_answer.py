def palindrome_of_length_n(text):
    if len(text) < 91:
        return set()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    text_lower = text.lower()
    for i in range(len(text) - 89):
        substr = text_lower[i:i + 91]
        if all((c.isalpha() for c in substr)):
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes