def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[29:99]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 6, i + 10):
            if j <= len(s) and s[i:j].isalpha() and is_palindrome(s[i:j].lower()):
                palindromes.add(s[i:j].lower())
    return palindromes