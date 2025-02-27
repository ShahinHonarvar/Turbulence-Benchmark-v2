def palindrome_of_length_n(s):

    def is_palindrome(x):
        return x == x[::-1]
    s = s.lower()
    length = 91
    palindromes = set()
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr.isalpha() and is_palindrome(substr):
            palindromes.add(substr)
    return palindromes