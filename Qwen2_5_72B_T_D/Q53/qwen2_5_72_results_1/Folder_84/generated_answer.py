def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    palindromes = set()
    n = 81
    for i in range(len(text)):
        for j in range(i + n, len(text) + 1):
            substring = text[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes