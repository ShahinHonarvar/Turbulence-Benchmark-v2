def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(3, 16):
        for start in range(0, 101):
            end = start + length
            substring = string[start:end]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes