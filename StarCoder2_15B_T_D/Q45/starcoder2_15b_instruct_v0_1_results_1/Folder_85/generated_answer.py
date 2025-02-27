def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(2, 9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 10):
                substring = string[i:k]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes