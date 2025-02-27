def palindromes_of_specific_lengths(string):
    palindromes = set()
    start_index = 36
    end_index = 92
    substring = string[start_index:end_index + 1]
    for length in range(10, 36):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes