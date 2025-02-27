def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(23, 37):
        for start in range(18, len(string) - length + 1):
            substring = string[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes