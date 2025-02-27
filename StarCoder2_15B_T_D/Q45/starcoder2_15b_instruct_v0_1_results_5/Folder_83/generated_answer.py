def palindromes_between_indices(string):
    string = string.lower()
    palindromes = set()
    for i in range(2, 10):
        for j in range(i + 1, 10):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes