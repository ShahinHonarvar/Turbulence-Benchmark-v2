def palindrome_of_length_at_least_n(text):

    def is_palindrome(s, start, end, letters_only=True):
        while start < end:
            if letters_only and (not s[start].isalpha() or not s[end].isalpha()):
                return False
            if s[start].lower() != s[end].lower():
                return False
            start, end = (start + 1, end - 1)
        return True
    palindromes = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 10, len(text) + 1):
            if is_palindrome(text, i, j):
                palindromes.add(text[i:j])
    return palindromes