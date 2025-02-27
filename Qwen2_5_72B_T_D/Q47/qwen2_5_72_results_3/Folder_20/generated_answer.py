def palindromes_of_specific_lengths(s):

    def is_palindrome(p):
        return p.lower() == p[::-1].lower()
    s = s[20:75]
    result = set()
    for i in range(len(s)):
        for j in range(i + 36, min(i + 43, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result