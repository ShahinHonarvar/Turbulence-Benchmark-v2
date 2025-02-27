def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[127:288 + 1]
    for length in range(119, 141 + 1):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes