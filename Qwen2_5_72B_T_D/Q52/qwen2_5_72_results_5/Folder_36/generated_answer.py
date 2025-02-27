def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    length = 338
    n = len(s)
    palindromes = set()
    for i in range(n - length + 1):
        sub = s[i:i + length]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes