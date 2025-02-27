def palindromes_of_specific_lengths(string):
    substring = string[39:95]
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes