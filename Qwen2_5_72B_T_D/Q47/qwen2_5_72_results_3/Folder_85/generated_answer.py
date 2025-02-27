def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    for length in range(6, 10):
        for start in range(29, 99 - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring.lower())
    return result