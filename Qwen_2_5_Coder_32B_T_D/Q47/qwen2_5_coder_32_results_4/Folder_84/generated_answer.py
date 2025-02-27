def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[23:78].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 13, min(i + 41, len(s) + 1)):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes