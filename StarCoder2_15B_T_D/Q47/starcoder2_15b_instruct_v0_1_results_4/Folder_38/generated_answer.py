def palindromes_of_specific_lengths(string):
    substring = string[18:88]
    palindromes = set()
    for length in range(38, 61):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes