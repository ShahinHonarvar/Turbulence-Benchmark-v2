def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    substring = s[32:72]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 21, min(i + 33, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes