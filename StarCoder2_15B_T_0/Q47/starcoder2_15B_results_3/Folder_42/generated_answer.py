def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[43:96]
    for length in range(18, 48):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes