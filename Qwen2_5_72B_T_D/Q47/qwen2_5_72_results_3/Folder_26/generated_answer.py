def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substr = s[24:85]
    found_palindromes = set()
    for length in range(21, 32):
        for start in range(len(substr) - length + 1):
            sub = substr[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                found_palindromes.add(sub)
    return found_palindromes