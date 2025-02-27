def palindromes_of_specific_lengths(string):
    substring = string[11:84]
    palindromes = set()
    for length in range(13, 67):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1] and window.isalpha():
                palindromes.add(window)
    return palindromes