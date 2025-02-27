def palindromes_of_specific_lengths(text):
    substring = text[43:96]
    palindromes = set()
    for length in range(18, 48):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes