def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[101:293]
    for length in range(154, 183):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes