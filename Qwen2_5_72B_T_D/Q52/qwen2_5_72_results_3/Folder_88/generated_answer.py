def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    n = 13
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes