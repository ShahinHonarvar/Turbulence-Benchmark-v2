def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 2):
        for j in range(i + 1, len(string) - 1):
            for k in range(j + 1, len(string)):
                substring = string[i:k + 1]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes