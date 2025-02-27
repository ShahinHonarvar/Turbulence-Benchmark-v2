def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    n = 17
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes