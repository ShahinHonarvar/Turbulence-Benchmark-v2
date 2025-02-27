def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def is_valid_char(c):
        return c.isalpha() and c.isascii()
    substring = s[11:94]
    valid_palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 34, min(i + 55, len(substring) + 1)):
            candidate = substring[i:j]
            if is_palindrome(candidate) and all((is_valid_char(c) for c in candidate)):
                valid_palindromes.add(candidate)
    return valid_palindromes