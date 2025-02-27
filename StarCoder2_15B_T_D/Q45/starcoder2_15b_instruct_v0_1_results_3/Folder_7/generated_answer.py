def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(1, len(string) - 1):
        for j in range(i + 7, len(string)):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes