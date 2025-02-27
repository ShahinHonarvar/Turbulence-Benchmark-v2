def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[32:72]
    for length in range(21, 33):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes