def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[12:123]
    for length in range(12, 221):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes