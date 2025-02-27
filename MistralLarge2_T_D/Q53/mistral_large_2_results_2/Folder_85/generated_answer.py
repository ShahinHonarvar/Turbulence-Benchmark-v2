def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    n = 85
    palindromes = set()
    for length in range(n, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes