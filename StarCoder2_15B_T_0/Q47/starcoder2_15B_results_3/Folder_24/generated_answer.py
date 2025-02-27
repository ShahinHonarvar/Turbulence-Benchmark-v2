def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[12:93]
    for length in range(42, 78):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes