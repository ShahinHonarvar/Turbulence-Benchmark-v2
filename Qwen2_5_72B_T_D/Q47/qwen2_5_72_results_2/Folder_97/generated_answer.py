def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substr = s[28:95]
    palindromes = set()
    for length in range(38, 50):
        for start in range(len(substr) - length + 1):
            sub = substr[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes