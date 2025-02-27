def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    n = 67
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes