def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[15:96]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 20, i + 67):
            if j > len(s):
                break
            candidate = s[i:j]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes