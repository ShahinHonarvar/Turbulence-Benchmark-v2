def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def is_valid_char(c):
        return c.isalpha()
    valid_substring = s[11:98]
    palindromes_set = set()
    for length in range(29, 63):
        for start in range(len(valid_substring) - length + 1):
            substring = valid_substring[start:start + length]
            if all((is_valid_char(c) for c in substring)) and is_palindrome(substring):
                palindromes_set.add(substring)
    return palindromes_set