def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(2, 6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 7):
                substring = string[i:k]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes