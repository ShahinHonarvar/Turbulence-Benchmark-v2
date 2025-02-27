def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[23:95]
    result = set()
    for i in range(len(s)):
        for j in range(i + 17, min(len(s), i + 56)):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                result.add(s[i:j].lower())
    return result