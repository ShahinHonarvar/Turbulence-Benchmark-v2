def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 46):
        substring = s[i:i + 51]
        if all((c.isalpha() for c in substring)):
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes