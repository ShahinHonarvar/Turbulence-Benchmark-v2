def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:10]
    for i in range(len(substring) - 2):
        for j in range(i + 3, min(i + 6, len(substring))):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes