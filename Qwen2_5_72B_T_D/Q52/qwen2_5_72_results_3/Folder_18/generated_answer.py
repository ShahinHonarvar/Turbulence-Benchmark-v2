def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    length = len(text)
    n = 392
    palindromes = set()
    for i in range(length - n + 1):
        substring = text[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes