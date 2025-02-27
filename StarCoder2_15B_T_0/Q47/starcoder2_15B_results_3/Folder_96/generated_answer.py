def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:301]
    for i in range(len(substring) - 50):
        for j in range(i + 50, min(i + 101, len(substring))):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes