def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(26, 30):
        for i in range(13, 100 - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes