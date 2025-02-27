def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = ''.join(filter(str.isalpha, text.lower()))
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 4, len(text) + 1):
            candidate = text[i:j]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes