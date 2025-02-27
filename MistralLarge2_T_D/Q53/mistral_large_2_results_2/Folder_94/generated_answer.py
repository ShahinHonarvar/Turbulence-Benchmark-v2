def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    n = 41
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes