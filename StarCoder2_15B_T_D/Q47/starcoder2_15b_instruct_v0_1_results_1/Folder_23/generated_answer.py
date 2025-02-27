def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[23:95]
    for length in range(17, 56):
        for start in range(len(substring) - length + 1):
            substring_slice = substring[start:start + length]
            if substring_slice == substring_slice[::-1]:
                palindromes.add(substring_slice)
    return palindromes