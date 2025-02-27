def palindrome_of_length_n(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s.lower()
    length = 475
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes