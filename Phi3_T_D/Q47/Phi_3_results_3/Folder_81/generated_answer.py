def palindromes_of_specific_lengths(s):
    s = s[12:123]
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1] and all(('a' <= c <= 'z' for c in sub)) and (12 <= len(sub) <= 220)
    for length in range(12, 221):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes