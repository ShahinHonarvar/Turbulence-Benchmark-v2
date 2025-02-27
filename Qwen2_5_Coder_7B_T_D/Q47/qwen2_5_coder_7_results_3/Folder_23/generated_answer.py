def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1] and sub.isalpha() and (17 <= len(sub) <= 55)
    s = s[23:95].lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 17, min(i + 56, len(s) + 1)) if is_palindrome(s[i:j])}