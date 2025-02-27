def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[10:101]
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes