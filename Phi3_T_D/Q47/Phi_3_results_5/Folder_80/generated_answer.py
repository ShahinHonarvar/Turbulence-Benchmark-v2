def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(35, 89):
        for length in range(24, 34):
            if i + length > 89:
                break
            substr = s[i:i + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes