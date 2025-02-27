def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    length = 72
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if is_palindrome(substring.lower()):
            palindromes.add(substring)
    return palindromes