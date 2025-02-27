def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    n = 22
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if is_palindrome(substring.lower()) and substring.isalpha():
                palindromes.add(substring)
    return palindromes