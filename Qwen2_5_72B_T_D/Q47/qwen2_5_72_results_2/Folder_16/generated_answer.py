def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    substring = s[15:87]
    palindromes = set()
    for length in range(51, 61):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and candidate.isalpha():
                palindromes.add(candidate.lower())
    return palindromes