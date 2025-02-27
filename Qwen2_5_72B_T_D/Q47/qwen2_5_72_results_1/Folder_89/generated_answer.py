def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[18:89]
    result = set()
    for i in range(len(s)):
        for j in range(12, 15):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub.isalpha() and is_palindrome(sub.lower()):
                    result.add(sub)
    return result