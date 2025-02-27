def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[17:96]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 13, min(start + 50, len(s) + 1)):
            substring = s[start:end].lower()
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes