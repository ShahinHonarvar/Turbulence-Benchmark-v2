def palindromes_of_specific_lengths(string):
    palindromes = set()
    length_range = range(39, 53)
    for length in length_range:
        for i in range(16, len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes