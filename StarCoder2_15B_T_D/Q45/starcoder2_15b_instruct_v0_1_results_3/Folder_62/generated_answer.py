def palindromes_between_indices(string):
    string = string.upper()
    palindromes = set()
    for i in range(0, len(string) - 8):
        for j in range(i + 7, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes