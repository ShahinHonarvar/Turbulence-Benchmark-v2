def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = s[44:100]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 13, min(i + 43, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes