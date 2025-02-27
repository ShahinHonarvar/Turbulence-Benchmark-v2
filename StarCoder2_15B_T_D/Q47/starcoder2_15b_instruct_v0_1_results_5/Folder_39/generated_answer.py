def palindromes_of_specific_lengths(string):
    substring = string[31:92]
    palindromes = set()
    for length in range(50, 54):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes