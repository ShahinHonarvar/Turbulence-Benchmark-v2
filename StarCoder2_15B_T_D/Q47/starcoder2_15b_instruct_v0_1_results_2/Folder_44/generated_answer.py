def palindromes_of_specific_lengths(string):
    substring = string[18:99]
    palindromes = set()
    for length in range(31, 52):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes