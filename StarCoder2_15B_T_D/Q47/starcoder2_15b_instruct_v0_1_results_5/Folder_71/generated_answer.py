def palindromes_of_specific_lengths(string):
    substring = string[18:66]
    palindromes = set()
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes