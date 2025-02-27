def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[35:89].lower()
    found_palindromes = set()
    for length in range(24, 34):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes