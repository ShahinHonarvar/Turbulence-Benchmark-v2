def palindrome_of_length_at_least_n(text):
    text = text.lower()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 42, len(text)):
            if is_palindrome(text[i:j + 1]):
                palindromes.add(text[i:j + 1])
    return palindromes