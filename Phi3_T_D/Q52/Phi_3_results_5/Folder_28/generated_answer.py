def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 42):
        if is_palindrome(s[i:i + 43]):
            palindromes.add(s[i:i + 43])
    return palindromes