def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 97, len(s)):
            substr = s[i:j + 1]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes