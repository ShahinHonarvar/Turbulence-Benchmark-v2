def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[11:98]
    palindromes = set()
    for length in range(29, 63):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr.isalpha() and is_palindrome(substr.lower()):
                palindromes.add(substr)
    return palindromes