def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_range = s[17:96]
    palindromes = set()
    for start in range(len(valid_range)):
        for end in range(start + 13, min(start + 50, len(valid_range) + 1)):
            substring = valid_range[start:end]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes