def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[32:72]
    palindromes = set()
    for length in range(21, 33):
        for start in range(len(text) - length + 1):
            substring = text[start:start + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring.lower())
    return palindromes