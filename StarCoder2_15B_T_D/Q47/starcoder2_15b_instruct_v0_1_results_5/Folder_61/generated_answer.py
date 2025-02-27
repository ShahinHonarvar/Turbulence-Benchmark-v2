def palindromes_of_specific_lengths(string):
    if not string:
        return set()
    substring = string[:31]
    lengths = range(20, 31)
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes