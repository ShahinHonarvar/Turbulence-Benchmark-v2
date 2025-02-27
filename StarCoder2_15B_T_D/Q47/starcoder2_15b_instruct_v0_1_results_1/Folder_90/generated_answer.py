def palindromes_of_specific_lengths(string):
    string = string[106:281]
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes