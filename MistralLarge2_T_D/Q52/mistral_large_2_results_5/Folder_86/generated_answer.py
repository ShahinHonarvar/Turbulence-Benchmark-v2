def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    length_n = 181
    palindromes = set()
    s_length = len(s)
    for i in range(s_length - length_n + 1):
        substring = s[i:i + length_n]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes