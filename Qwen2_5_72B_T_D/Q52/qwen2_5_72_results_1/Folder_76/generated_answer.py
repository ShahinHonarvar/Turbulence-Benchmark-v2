def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    length = 257
    palindromes = set()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes