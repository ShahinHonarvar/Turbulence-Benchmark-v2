def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    n = 18
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub.lower())
    return palindromes