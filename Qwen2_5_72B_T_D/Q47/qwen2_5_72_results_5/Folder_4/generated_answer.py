def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[12:93]
    result = set()
    for i in range(len(s)):
        for j in range(i + 17, min(i + 67, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                result.add(substring)
    return result