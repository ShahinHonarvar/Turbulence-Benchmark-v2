def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t.lower() == t.lower()[::-1]
    substring = s[41:90]
    palindromes = set()
    for i in range(23, 39):
        for j in range(len(substring) - i + 1):
            candidate = substring[j:j + i]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes