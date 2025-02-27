def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    s = ''.join((c for c in s if c.isalpha()))
    for i in range(len(s) - 16):
        sub = s[i:i + 17]
        if is_palindrome(sub):
            palindromes.add(sub)
    return palindromes