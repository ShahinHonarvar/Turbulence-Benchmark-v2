def palindromes_of_specific_lengths(string):
    substring = string[17:96]
    palindromes = set()
    for i in range(len(substring) - 12):
        for length in range(13, 50):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes