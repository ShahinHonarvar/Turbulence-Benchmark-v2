def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[20:75]
    for length in range(36, 43):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes