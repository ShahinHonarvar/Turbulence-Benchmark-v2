def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_range = s[12:123]
    found_palindromes = set()
    for start in range(len(valid_range)):
        for end in range(start + 12, min(start + 221, len(valid_range) + 1)):
            substring = valid_range[start:end]
            if substring.isalpha() and is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes