def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[12:123]
    for length in range(12, 221):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                if window.isalpha():
                    palindromes.add(window.lower())
    return palindromes