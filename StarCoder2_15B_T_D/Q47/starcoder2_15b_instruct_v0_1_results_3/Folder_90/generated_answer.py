def palindromes_of_specific_lengths(text):
    substring = text[106:281]
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes