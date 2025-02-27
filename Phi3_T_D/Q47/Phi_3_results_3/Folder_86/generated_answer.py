def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    palindromes = set()
    for length in range(34, 56):
        for i in range(30, 96 - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring) and substring.isalpha() and (substring.isalpha() == substring.lower()):
                palindromes.add(substring.lower())
    return palindromes