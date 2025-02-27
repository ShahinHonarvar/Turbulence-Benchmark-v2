def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    text = ''.join((c for c in text if c.isalpha())).lower()
    length = len(text)
    for i in range(length):
        for j in range(i + 11, length + 1):
            substring = text[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes