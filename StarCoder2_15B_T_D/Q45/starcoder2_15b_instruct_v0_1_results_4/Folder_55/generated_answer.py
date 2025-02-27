def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 2):
        for j in range(i + 3, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes