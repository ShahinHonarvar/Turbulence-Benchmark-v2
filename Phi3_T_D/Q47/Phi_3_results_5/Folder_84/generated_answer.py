def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    palindromes = set()
    substr = s[23:78]
    for length in range(13, 41):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes