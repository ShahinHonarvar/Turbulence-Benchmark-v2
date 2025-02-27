def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = ''.join(filter(str.isalpha, text.lower()))
    n = len(text)
    min_length = 19
    palindromes = set()
    for i in range(n):
        for j in range(i + min_length, n + 1):
            if is_palindrome(text[i:j]):
                palindromes.add(text[i:j])
    return palindromes