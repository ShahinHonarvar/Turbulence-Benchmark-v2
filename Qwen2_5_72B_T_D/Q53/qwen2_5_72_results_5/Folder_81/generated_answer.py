def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = len(text)
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(n):
        for j in range(i + 32, n):
            candidate = text[i:j + 1]
            if is_palindrome(candidate) and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes