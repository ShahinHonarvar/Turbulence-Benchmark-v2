def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substr = s[30:85].lower()
    palindromes = set()
    for length in range(12, 21):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes