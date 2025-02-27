def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 37, len(s) + 1):
            substring = s[i:j]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes