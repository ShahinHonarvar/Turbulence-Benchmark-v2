def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 20):
        sub = s[i:i + 21]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes