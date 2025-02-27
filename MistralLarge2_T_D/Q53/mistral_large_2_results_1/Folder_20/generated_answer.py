def palindrome_of_length_at_least_n(string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    n = len(string)
    for i in range(n):
        for j in range(i + 66, n + 1):
            substring = string[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring.lower())
    return palindromes