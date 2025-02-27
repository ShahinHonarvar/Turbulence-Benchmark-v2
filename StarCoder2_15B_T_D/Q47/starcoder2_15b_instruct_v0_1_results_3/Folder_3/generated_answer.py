def palindromes_of_specific_lengths(string):
    substring = string[27:96]
    lengths = set(range(49, 52))
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            if j - i not in lengths:
                continue
            window = substring[i:j]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes