def palindromes_of_specific_lengths(string):
    substring = string[22:96]
    palindromes = set()
    for i in range(len(substring) - 51):
        for length in range(52, 56):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes