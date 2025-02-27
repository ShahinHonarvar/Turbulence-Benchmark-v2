def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[15:87]
    for i in range(len(substring) - 50):
        for length in range(51, 61):
            window = substring[i:i + length]
            if window == window[::-1] and window.isalpha():
                palindromes.add(window)
    return palindromes