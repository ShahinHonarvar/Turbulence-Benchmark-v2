def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[:8]
    palindromes = set()
    for length in range(4, 6):
        for start in range(0, 8 - length + 1):
            substr = s[start:start + length]
            if substr.isalpha() and is_palindrome(substr.lower()):
                palindromes.add(substr)
    return palindromes