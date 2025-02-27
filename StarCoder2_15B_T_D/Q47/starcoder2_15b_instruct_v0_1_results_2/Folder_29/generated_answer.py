def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[15:95]
    for length in range(18, 74):
        for start in range(len(substring) - length + 1):
            palindrome = substring[start:start + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes