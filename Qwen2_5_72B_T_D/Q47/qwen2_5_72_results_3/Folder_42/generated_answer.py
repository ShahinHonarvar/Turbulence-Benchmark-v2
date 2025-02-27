def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[43:96]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 18, min(i + 48, len(s) + 1)):
            substring = s[i:j].lower()
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes