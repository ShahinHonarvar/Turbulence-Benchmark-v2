def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(5, 81):
        for start in range(21):
            end = start + length
            substring = string[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes