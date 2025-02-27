def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    lower, upper = (10, 100)
    min_len, max_len = (10, 50)
    s = s[lower:upper + 1]
    for i in range(len(s)):
        for j in range(i + min_len, min(i + max_len + 1, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                result.add(substring)
    return result