def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    length = len(s)
    s = s.lower()
    for i in range(length):
        for j in range(i + 70, length + 1):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes