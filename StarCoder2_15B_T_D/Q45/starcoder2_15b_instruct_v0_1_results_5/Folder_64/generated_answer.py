def palindromes_between_indices(string):
    string = string.upper()
    palindromes = set()
    for i in range(4, len(string) - 4):
        for j in range(i + 5, len(string) - 3):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes