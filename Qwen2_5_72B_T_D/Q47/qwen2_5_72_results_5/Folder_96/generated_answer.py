def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[100:301]
    result = set()
    for i in range(len(s)):
        for j in range(i + 50, min(i + 101, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and is_palindrome(substr.lower()):
                result.add(substr)
    return result