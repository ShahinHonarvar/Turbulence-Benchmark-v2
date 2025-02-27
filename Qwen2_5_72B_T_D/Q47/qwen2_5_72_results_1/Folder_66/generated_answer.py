def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[32:80]
    palindromes = set()
    for length in range(35, 42):
        for start in range(len(substring) - length + 1):
            part = substring[start:start + length]
            if part.isalpha() and is_palindrome(part.lower()):
                palindromes.add(part)
    return palindromes