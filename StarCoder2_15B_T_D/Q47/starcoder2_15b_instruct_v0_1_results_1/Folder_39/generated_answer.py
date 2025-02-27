def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(31, 92):
        for j in range(i + 50, i + 54):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes