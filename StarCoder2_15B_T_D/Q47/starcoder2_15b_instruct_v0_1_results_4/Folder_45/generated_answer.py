def palindromes_of_specific_lengths(string):
    substring = string[70:141]
    palindromes = set()
    for length in range(3, 61):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes