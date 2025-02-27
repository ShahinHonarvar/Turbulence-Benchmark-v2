def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[1:10].lower()
    palindromes = set()
    for length in range(3, 8):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes