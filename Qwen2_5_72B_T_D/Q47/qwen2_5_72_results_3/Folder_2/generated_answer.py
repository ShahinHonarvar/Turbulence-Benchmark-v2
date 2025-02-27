def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[10:60].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 18, min(i + 37, len(s) + 1)):
            if s[i:j].isalpha() and is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result