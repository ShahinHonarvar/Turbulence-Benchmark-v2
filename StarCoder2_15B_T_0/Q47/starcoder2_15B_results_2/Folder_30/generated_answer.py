def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[14:91]
    for length in range(55, 72):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes