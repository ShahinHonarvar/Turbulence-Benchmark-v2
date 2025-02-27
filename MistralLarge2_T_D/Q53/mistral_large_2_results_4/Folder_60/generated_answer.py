def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    length = len(s)
    s = ''.join((c.lower() for c in s if c.isalpha()))
    for i in range(length):
        for j in range(i + 80, length + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes