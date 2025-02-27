def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    s = s[23:95]
    result = set()
    for i in range(len(s)):
        for j in range(i + 17, min(i + 56, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                result.add(substring)
    return result