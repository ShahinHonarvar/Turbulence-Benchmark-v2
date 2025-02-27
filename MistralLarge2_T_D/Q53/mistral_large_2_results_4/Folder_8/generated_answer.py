def palindrome_of_length_at_least_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 45, length + 1):
            substring = s[i:j]
            if is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes