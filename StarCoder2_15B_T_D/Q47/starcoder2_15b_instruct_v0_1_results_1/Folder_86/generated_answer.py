def palindromes_of_specific_lengths(string):
    substring = string[30:96]
    palindromes = set()
    for i in range(len(substring) - 34):
        for j in range(34, 56):
            if i + j > len(substring):
                break
            substring_part = substring[i:i + j]
            if substring_part == substring_part[::-1]:
                palindromes.add(substring_part)
    return palindromes