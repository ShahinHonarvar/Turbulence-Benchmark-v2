def palindromes_of_specific_lengths(string):
    substring = string[65:100]
    palindromes = set()
    for length in range(26, 34):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes