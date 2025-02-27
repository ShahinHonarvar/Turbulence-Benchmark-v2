def palindromes_of_specific_lengths(string):
    substring = string[11:97]
    palindromes = set()
    for length in range(45, 53):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes