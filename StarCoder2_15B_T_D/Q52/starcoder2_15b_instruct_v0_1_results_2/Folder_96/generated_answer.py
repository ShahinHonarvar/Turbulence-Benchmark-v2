def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    n = 83
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes