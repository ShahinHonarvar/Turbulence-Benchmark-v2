def palindromes_of_specific_lengths(string):
    lower_string = string.lower()
    palindromes = set()
    for length in range(21, 32):
        for i in range(24, 85 - length + 1):
            substring = lower_string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes