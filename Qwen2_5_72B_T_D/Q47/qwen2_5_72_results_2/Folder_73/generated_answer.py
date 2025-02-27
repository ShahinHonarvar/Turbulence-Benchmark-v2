def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def valid_chars(sub):
        return all((c.isalpha() and (c.islower() or c.isupper()) for c in sub))
    result = set()
    for length in range(22, 34):
        for start in range(21, 63 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and valid_chars(substring):
                result.add(substring)
    return result