def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[200:301]
    for length in range(10, 51):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes