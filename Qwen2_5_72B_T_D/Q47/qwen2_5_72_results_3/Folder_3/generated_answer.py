def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_range = s[27:96]
    palindromes = set()
    for length in range(49, 52):
        for start in range(len(valid_range) - length + 1):
            substring = valid_range[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes