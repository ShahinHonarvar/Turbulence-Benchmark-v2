def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[100:296]
    result = set()
    for i in range(len(s)):
        for j in range(i + 136, min(i + 161, len(s) + 1)):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub.lower()):
                result.add(sub)
    return result