def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substr = s[44:100]
    palindromes = set()
    for length in range(13, 43):
        for start in range(len(substr) - length + 1):
            sub = substr[start:start + length]
            if sub.isalpha() and is_palindrome(sub.lower()):
                palindromes.add(sub)
    return palindromes