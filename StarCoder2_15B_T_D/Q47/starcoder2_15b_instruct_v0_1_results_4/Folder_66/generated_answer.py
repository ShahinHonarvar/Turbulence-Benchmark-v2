def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[32:80]
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes