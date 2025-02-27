def palindrome_of_length_at_least_n(text):
    text = text.lower()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    n = 26
    for i in range(len(text)):
        for j in range(i + n, len(text) + 1):
            if is_palindrome(text[i:j]):
                palindromes.add(text[i:j])
    return palindromes