def palindrome_of_length_n(s):
    s = s.lower()
    n = 96
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes