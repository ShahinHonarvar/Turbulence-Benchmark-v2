def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    palindromes = set()
    n = 41
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes