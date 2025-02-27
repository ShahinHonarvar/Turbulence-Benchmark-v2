def palindrome_of_length_at_least_n(string):

    def is_palindrome(s):
        return s == s[::-1]
    n = 46
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = string[i:j]
            if is_palindrome(substring.lower()) and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes