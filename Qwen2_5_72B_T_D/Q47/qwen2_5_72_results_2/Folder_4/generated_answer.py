def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[12:93]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 17, min(i + 67, len(s) + 1)):
            if s[i:j].isalpha() and is_palindrome(s[i:j]):
                palindromes.add(s[i:j].lower())
    return palindromes