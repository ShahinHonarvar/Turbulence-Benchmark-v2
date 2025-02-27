def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[155:284]
    for length in range(104, 121):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes