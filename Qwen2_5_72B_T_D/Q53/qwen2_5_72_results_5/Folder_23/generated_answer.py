def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    length = len(text)
    palindromes = set()
    for i in range(length):
        for j in range(i + 19, length + 1):
            substring = text[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes