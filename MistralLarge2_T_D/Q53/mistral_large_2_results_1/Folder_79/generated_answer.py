def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = ''.join((c for c in s if c.isalpha()))
    n = 17
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes