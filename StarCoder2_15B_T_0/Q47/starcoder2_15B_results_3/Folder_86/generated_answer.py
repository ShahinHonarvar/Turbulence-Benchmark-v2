def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[30:96]
    for length in range(34, 56):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes