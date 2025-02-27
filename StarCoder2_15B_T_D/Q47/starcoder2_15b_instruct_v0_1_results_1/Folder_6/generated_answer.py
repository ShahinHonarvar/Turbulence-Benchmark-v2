def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(40, 48):
        for start in range(45, len(string) - length + 1):
            substring = string[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes