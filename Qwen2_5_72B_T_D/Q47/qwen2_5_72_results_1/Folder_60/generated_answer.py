def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substr = s[23:83]
    palindromes = set()
    for length in range(32, 35):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes