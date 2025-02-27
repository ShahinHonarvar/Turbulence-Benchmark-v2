def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[:101]
    palindromes = set()
    for length in range(3, 16):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                if all((ch.isalpha() for ch in palindrome)):
                    palindromes.add(palindrome)
    return palindromes