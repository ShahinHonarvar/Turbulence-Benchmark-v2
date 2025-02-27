def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(10):
        for j in range(i + 3, min(i + 6, len(string))):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes