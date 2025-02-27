def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[11:84]
    for length in range(13, 67):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes