def palindromes_of_specific_lengths(string):
    substring = string[31:75]
    palindromes = set()
    for length in range(23, 40):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes