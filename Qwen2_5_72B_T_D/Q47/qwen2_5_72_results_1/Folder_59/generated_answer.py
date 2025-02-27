def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[:101]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 16, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and is_palindrome(substr.lower()):
                palindromes.add(substr.lower())
    return palindromes