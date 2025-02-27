def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substr = s[30:96]
    palindromes = set()
    for length in range(34, 56):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes