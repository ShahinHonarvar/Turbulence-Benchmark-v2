def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[39:95]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    palindromes = set()
    for length in range(14, 53):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes