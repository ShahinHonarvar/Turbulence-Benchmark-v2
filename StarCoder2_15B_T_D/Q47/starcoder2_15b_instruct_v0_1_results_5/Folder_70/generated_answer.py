def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[10:71]
    for length in range(24, 53):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes