def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[41:90]
    palindromes = set()
    for length in range(23, 39):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes