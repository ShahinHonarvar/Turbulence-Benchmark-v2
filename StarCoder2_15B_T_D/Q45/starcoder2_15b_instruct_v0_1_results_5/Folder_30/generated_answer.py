def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 4 + 1):
        for j in range(i + 4, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes