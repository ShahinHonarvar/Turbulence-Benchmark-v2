def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]

    def is_valid_char(c):
        return c.isalpha() and c.isascii()
    substring = s[26:85]
    palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 29, start + 47):
            if end < len(substring):
                candidate = substring[start:end + 1]
                if all((is_valid_char(c) for c in candidate)) and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes