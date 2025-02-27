def palindromes_of_specific_lengths(string):
    palindromes = set()
    length_range = range(6, 9)
    for length in length_range:
        for i in range(10, len(string) - 74):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes