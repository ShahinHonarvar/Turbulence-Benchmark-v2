def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[11:97]
    for length in range(45, 53):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes