def palindrome_of_length_at_least_n(text):
    text = text.lower()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    n = len(text)
    for i in range(n):
        for j in range(i + 99, n):
            substring = text[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes