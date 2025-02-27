def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[30:96]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 34, min(start + 56, len(s) + 1)):
            sub = s[start:end]
            if sub.isalpha() and is_palindrome(sub.lower()):
                palindromes.add(sub)
    return palindromes