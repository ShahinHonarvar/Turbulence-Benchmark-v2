def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    s = s[10:60]
    palindromes = set()
    for length in range(18, 37):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes