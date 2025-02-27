def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    palindromes = set()
    for length in range(50, 101):
        for i in range(100, 301 - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring.lower()):
                palindromes.add(substring.lower())
    return palindromes