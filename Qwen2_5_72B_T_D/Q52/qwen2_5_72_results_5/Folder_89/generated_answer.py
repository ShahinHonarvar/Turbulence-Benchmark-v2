def palindrome_of_length_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = ''.join(filter(str.isalpha, text.lower()))
    n = 37
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes