def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[17:96]
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes