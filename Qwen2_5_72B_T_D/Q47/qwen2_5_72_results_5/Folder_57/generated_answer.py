def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    s = s[16:95].lower()
    for length in range(39, 53):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result