def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 90, len(s)):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes