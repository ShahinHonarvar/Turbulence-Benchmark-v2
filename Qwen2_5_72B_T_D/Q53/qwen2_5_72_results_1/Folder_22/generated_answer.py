def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 96, len(s)):
            subst = s[i:j + 1]
            if is_palindrome(subst):
                palindromes.add(subst)
    return palindromes