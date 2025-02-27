def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    considered_range = s[200:301]
    palindromes = set()
    for length in range(10, 51):
        for start in range(len(considered_range) - length + 1):
            substring = considered_range[start:start + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes