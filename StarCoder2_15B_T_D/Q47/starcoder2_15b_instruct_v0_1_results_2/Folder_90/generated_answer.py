def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[106:281]
    for i in range(len(substring) - 136):
        for length in range(136, 152):
            if i + length > len(substring):
                continue
            palindrome = substring[i:i + length]
            if palindrome == palindrome[::-1]:
                if all((ch.isalpha() for ch in palindrome)):
                    palindromes.add(palindrome.lower())
    return palindromes