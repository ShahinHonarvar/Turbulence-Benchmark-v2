def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[27:78]
    for length in range(18, 20):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes