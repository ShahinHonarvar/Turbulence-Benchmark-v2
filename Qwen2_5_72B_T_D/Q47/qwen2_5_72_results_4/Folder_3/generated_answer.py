def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[27:96]
    result = set()
    for length in range(49, 52):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result