def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(4, len(string) - 3):
        for j in range(i + 3, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes