def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    n = 147
    length = len(s)
    palindromes = set()
    for i in range(length - n + 1):
        sub = s[i:i + n]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes