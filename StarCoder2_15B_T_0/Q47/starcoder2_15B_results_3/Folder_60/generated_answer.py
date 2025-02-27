def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[23:83]
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes