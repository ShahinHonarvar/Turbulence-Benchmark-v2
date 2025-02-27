def palindromes_of_specific_lengths(string):
    substring = string[119:257]
    palindromes = set()
    for length in range(104, 124):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes