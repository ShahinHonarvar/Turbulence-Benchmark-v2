def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(5, len(string) - 1):
        for j in range(i + 1, len(string)):
            substring = string[i:j + 1]
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes