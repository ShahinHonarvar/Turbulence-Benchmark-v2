def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[20:75]
    for length in range(36, 43):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes