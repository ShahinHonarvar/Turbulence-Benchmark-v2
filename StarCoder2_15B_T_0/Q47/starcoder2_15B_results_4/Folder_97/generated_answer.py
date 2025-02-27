def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[28:95]
    for length in range(38, 50):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes