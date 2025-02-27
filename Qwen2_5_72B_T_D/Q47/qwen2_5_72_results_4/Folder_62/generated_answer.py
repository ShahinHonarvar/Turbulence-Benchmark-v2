def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def is_valid_length(sub):
        return 52 <= len(sub) <= 56

    def is_valid_char(c):
        return c.isalpha() and c.isascii()
    valid_substring = s[26:88]
    palindromes = set()
    for i in range(len(valid_substring)):
        for j in range(i + 52, i + 57):
            if j <= len(valid_substring):
                sub = valid_substring[i:j]
                if is_palindrome(sub) and is_valid_length(sub) and all((is_valid_char(c) for c in sub)):
                    palindromes.add(sub)
    return palindromes