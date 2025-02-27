def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[29:99]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 6, min(i + 10, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes