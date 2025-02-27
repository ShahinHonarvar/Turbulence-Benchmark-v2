def palindrome_of_length_n(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    n = 407
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes