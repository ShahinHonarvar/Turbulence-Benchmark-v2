def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(len(string) - 7):
        substring = string[i:i + 8]
        for j in range(4, 6):
            for k in range(len(substring) - j + 1):
                window = substring[k:k + j]
                if window == window[::-1]:
                    palindromes.add(window)
    return palindromes