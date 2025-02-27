def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:201]
    for length in range(5, 11):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes