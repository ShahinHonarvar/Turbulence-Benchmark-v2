def palindromes_of_specific_lengths(s):
    substring = s[12:123]
    palindromes = set()
    for length in range(12, 221):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1] and all((c.isalpha() for c in palindrome)):
                palindromes.add(palindrome)
    return palindromes