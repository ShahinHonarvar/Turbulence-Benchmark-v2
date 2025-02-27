def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(6, 9):
        for start in range(10, len(string) - 74):
            substring = string[start:start + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes