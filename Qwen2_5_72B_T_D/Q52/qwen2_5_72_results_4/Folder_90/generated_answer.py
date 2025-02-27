def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    length = 318
    n = len(s)
    palindromes = set()
    if n < length:
        return palindromes
    for i in range(n - length + 1):
        sub = s[i:i + length]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes