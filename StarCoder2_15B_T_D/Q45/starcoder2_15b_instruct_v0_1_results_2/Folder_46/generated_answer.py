def palindromes_between_indices(string):
    string = string.upper()
    palindromes = set()
    for i in range(len(string) - 5):
        for j in range(i + 6, len(string)):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes