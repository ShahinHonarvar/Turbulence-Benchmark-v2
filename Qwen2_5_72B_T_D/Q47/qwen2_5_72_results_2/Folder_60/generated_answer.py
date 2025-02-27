def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s_sub = s[23:83]
    palindromes = set()
    for length in range(32, 35):
        for i in range(len(s_sub) - length + 1):
            substring = s_sub[i:i + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes