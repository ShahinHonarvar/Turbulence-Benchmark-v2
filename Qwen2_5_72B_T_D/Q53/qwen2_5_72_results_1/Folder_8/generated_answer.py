def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text.lower()
    palindromes = set()
    n = 45
    for i in range(len(text)):
        for j in range(i + n, len(text) + 1):
            segment = text[i:j]
            if segment.isalpha() and is_palindrome(segment):
                palindromes.add(segment)
    return palindromes