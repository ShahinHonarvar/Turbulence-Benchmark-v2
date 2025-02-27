def palindromes_of_specific_lengths(s):

    def is_palindrome(p):
        return p == p[::-1]
    result = set()
    s = s[18:99].lower()
    for i in range(len(s)):
        for j in range(i + 31, min(i + 52, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result