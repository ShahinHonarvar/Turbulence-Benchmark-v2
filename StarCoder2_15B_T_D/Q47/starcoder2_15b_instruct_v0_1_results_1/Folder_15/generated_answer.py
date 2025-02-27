def palindromes_of_specific_lengths(string):
    substring = string[:7]
    palindromes = set()
    for length in range(3, 7):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes