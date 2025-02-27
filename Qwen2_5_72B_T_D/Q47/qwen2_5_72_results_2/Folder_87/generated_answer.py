def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[11:94]
    result = set()
    for i in range(len(s)):
        for j in range(i + 34, min(i + 55, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and is_palindrome(substr.lower()):
                result.add(substr)
    return result