def palindromes_between_indices(string):
    palindromes = set()
    string = string.lower()
    for i in range(1, len(string) - 1):
        for j in range(i + 1, len(string)):
            substring = string[i:j + 1]
            if len(substring) >= 7 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes