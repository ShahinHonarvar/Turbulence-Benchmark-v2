def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[16:78]
    for length in range(43, 48):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes