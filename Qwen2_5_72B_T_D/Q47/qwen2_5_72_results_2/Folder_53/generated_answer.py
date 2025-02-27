def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[1:300].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 11, len(s) + 1)):
            if s[i:j].isalpha() and is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes