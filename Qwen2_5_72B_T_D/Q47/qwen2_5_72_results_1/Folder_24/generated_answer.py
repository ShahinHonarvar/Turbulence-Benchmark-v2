def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[12:93]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 42, min(i + 78, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and is_palindrome(substr.lower()):
                palindromes.add(substr)
    return palindromes