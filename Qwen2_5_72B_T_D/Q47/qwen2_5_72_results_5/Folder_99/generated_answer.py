def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[127:289]
    result = set()
    for i in range(len(s)):
        for j in range(i + 119, i + 142):
            if j <= len(s):
                sub = s[i:j].lower()
                if sub.isalpha() and is_palindrome(sub):
                    result.add(sub)
    return result