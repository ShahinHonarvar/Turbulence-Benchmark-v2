def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[29:97]
    palindromes = set()
    for i in range(12, 19):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i].lower()
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes