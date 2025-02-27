def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1] and sub.isalpha()
    palindromes = {sub for i in range(3, 6) for sub in (s[j:j + i] for j in range(6) if is_palindrome(s[j:j + i]))}
    return palindromes