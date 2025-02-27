def palindrome_of_length_at_least_n(string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    palindromes = set()
    n = string.lower()
    length = len(n)
    for i in range(length):
        for j in range(i + 98, length + 1):
            substring = n[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes