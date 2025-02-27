def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = ''.join(filter(str.isalpha, s))
    n = 423
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_palindrome(sub):
            palindromes.add(sub)
    return palindromes