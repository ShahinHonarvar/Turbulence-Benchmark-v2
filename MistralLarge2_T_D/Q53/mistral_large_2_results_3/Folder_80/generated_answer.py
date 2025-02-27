def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 30, n + 1):
            substring = s[i:j]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes