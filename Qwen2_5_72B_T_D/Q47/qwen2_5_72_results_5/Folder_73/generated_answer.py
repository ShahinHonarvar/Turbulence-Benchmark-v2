def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[21:63]
    palindromes = set()
    for length in range(22, 34):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes