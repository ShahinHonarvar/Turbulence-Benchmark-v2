def palindromes_of_specific_lengths(string):
    substring = string[119:257]
    palindromes = set()
    for length in range(104, 124):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                if all((ch.isalpha() for ch in palindrome)):
                    palindromes.add(palindrome)
    return palindromes