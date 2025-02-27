def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[125:284]
    for i in range(109, 127):
        for j in range(len(substring) - i + 1):
            window = substring[j:j + i]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes