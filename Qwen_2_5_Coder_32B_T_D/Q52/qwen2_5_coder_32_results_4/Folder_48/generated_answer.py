def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    n = 186
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_palindrome(sub) and sub.isalpha():
            palindromes.add(sub)
    return palindromes