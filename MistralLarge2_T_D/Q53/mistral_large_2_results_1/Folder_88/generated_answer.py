def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    n = 27
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes