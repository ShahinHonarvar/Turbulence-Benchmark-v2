def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[18:88].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 38, min(i + 61, len(s) + 1)):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                result.add(s[i:j])
    return result