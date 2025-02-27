def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s)):
        for j in range(i + 49, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes