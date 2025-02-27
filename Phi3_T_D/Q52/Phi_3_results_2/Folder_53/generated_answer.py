def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    length = 68
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - length + 1):
        if is_palindrome(s[i:i + length]):
            palindromes.add(s[i:i + length])
    return palindromes