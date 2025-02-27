def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    palindromes = set()
    n = len(text)
    for i in range(n):
        for j in range(i + 52, n):
            candidate = text[i:j + 1]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes