def palindrome_of_length_n(s):
    s = s.lower()
    length = 173
    n = len(s)
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(n - length + 1):
        sub = s[i:i + length]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes