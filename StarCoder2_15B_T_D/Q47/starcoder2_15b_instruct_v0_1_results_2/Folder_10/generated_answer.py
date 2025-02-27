def palindromes_of_specific_lengths(string):
    substring = string[16:61]
    palindromes = set()
    for length in range(16, 40):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                if all((c.isalpha() for c in window)):
                    palindromes.add(window)
    return palindromes