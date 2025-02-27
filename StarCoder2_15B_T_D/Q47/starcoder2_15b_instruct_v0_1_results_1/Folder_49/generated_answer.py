def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string.lower()
    for i in range(10, 101):
        for j in range(i, 101):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes