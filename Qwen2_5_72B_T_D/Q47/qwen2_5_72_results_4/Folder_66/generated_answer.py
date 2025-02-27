def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substr = s[32:80]
    palindromes = set()
    for length in range(35, 42):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length].lower()
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes