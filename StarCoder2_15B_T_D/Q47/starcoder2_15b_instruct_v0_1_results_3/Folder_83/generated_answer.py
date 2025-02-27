def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[75:96]
    for i in range(len(substring) - 6):
        for j in range(i + 6, len(substring) + 1):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes