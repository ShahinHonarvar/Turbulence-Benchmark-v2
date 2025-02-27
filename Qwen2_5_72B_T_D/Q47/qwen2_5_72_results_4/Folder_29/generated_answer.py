def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[15:95]
    palindromes = set()
    for i in range(18, 74):
        for start in range(len(s) - i + 1):
            sub = s[start:start + i]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes