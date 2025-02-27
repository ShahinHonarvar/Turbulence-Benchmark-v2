def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[100:296].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 136, i + 161):
            if j <= len(s):
                substring = s[i:j]
                if substring.isalpha() and is_palindrome(substring):
                    result.add(substring)
    return result