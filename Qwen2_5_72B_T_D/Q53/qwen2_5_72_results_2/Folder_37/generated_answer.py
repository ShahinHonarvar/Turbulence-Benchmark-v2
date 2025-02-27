def palindrome_of_length_at_least_n(text):
    text = text.lower()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 66, len(text)):
            substring = text[i:j + 1]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes