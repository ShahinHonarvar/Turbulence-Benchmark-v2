def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 474):
        if is_palindrome(s[start:start + 475]):
            palindromes.add(s[start:start + 475])
    return palindromes