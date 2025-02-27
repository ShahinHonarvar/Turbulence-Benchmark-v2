def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[36:93]
    for length in range(10, 36):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes