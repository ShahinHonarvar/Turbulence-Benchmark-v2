def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[30:96]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(34, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes