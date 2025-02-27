def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    s = ''.join(filter(str.isalpha, s))
    n = 42
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j].lower())
    return palindromes