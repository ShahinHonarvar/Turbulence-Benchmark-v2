def palindromes_of_specific_lengths(string):
    substring = string[30:96]
    palindromes = set()
    for length in range(34, 56):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes