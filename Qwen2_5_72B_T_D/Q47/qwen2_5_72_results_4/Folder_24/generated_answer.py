def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    subset = s[12:93]
    palindromes = set()
    for length in range(42, 78):
        for start in range(len(subset) - length + 1):
            part = subset[start:start + length]
            if part.isalpha() and is_palindrome(part.lower()):
                palindromes.add(part)
    return palindromes