def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[11:94]
    result = set()
    for length in range(34, 55):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result