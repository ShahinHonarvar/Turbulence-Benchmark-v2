def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 180):
        sub = s[i:i + 181]
        if is_palindrome(sub) and sub.isalpha():
            palindromes.add(sub)
    return palindromes