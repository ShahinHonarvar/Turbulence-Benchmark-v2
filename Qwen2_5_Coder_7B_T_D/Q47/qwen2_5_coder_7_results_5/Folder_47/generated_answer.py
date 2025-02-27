def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1] and sub.isalpha()
    s = s[39:95].lower()
    palindromes = {s[i:i + j] for j in range(14, 53) for i in range(len(s) - j + 1) if is_palindrome(s[i:i + j])}
    return palindromes