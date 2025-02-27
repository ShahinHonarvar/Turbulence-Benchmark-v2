def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[41:90]
    for i in range(len(substring) - 23):
        for j in range(i + 23, min(i + 39, len(substring))):
            window = substring[i:j]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes