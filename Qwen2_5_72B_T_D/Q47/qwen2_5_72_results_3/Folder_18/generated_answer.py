def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[11:84]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 13, min(i + 67, len(s) + 1)):
            if s[i:j].isalpha() and is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes