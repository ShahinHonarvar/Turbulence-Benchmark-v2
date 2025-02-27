def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(14, 53):
        for start in range(40, 95 - length + 1):
            substring = string[start:start + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes