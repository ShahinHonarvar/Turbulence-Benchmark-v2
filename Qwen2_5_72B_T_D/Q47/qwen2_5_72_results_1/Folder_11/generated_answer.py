def palindromes_of_specific_lengths(s):

    def is_palindrome(p):
        return p.lower() == p.lower()[::-1]
    valid_range = s[24:98]
    found_palindromes = set()
    for length in range(10, 37):
        for start in range(len(valid_range) - length + 1):
            substring = valid_range[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes