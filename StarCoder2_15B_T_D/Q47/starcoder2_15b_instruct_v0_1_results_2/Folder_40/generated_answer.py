def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(6):
        for j in range(i + 3, i + 6):
            for k in range(i, j):
                substring = string[i:j]
                if substring[k] == substring[-k - 1]:
                    palindromes.add(substring)
    return palindromes