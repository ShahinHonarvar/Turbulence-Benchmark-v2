def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[130:296]
    palindromes = set()
    for i in range(103, 159):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes