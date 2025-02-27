def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[3:301]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 29, len(s)):
            substring = s[i:j + 1]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes