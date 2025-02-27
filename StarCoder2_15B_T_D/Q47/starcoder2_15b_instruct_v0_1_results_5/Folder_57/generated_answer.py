def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[16:95]
    for i in range(len(substring) - 39):
        for j in range(39, 53):
            if substring[i:i + j] == substring[i:i + j][::-1]:
                palindrome = substring[i:i + j].lower()
                if all((ch.isalpha() for ch in palindrome)):
                    palindromes.add(palindrome)
    return palindromes