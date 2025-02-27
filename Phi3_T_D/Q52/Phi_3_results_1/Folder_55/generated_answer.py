def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = {s[i:i + 97].lower() for i in range(len(s) - 96) if s[i:i + 97].isalpha() and is_palindrome(s[i:i + 97])}
    return palindromes