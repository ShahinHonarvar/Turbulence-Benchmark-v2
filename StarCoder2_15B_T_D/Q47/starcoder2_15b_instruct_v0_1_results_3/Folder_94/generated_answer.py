def palindromes_of_specific_lengths(string):
    substring = string[40:95]
    palindromes = set()
    for length in range(45, 52):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes