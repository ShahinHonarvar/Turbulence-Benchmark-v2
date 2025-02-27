def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[127:289]
    for length in range(119, 142):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes