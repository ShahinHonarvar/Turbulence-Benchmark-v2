def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    valid_range = s[22:96]
    palindromes = set()
    for length in range(52, 56):
        for start in range(len(valid_range) - length + 1):
            substring = valid_range[start:start + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes