def palindromes_of_specific_lengths(string):
    string = string[65:100]
    palindromes = set()
    for i in range(len(string) - 25):
        for length in range(26, 34):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes