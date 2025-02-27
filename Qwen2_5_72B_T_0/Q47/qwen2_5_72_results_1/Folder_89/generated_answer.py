def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    for length in range(12, 15):
        for start in range(18, 89 - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring.lower())
    return valid_palindromes