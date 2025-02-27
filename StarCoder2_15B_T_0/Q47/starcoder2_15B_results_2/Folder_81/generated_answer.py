def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[12:123]
    for length in range(12, 221):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes