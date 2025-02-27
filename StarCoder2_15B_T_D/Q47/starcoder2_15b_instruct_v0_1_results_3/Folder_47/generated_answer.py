def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[39:95]
    lengths = range(14, 53)
    for length in lengths:
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes