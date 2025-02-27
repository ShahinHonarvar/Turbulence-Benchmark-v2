def palindromes_of_specific_lengths(string):
    substring = string[2:9]
    palindromes = set()
    for i in range(len(substring) - 3):
        for j in range(i + 3, i + 5):
            window = substring[i:j]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes