def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    text = text[16:78].lower()
    palindromes = set()
    for length in range(43, 48):
        for start in range(len(text) - length + 1):
            substring = text[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes