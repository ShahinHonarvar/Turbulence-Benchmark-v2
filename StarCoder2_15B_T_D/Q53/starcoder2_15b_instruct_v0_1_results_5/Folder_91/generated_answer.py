def palindrome_of_length_at_least_n(string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    n = 7
    for i in range(len(string) - n + 1):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes