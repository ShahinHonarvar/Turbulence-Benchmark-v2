def palindromes_between_indices(string):
    palindromes = set()
    for i in range(2, len(string) - 1):
        for j in range(i + 1, min(i + 6, len(string))):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes