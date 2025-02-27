def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[63:71]
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                if all((ch.isalpha() for ch in palindrome)):
                    palindromes.add(palindrome)
    return palindromes