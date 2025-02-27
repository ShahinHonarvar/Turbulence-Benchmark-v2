def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[33:86]
    for length in range(26, 32):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes