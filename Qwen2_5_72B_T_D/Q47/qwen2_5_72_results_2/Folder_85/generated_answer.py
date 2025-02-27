def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substr = s[29:99]
    palindromes = set()
    for length in range(6, 10):
        for start in range(len(substr) - length + 1):
            sub = substr[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes