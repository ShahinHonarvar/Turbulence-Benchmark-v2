def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    s = s[26:91].lower()
    for i in range(len(s)):
        for j in range(i + 27, min(i + 59, len(s) + 1)):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                result.add(s[i:j])
    return result