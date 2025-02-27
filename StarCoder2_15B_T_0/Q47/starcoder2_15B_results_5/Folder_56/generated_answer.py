def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(3, 8):
        for i in range(1, len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes