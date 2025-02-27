def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[:11]
    result = set()
    for length in range(3, 6):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length].lower()
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result