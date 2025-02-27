def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(len(string) - 4):
        substring = string[i:i + 5]
        for j in range(3, 5):
            for k in range(len(substring) - j):
                window = substring[k:k + j]
                if window == window[::-1]:
                    palindromes.add(window)
    return palindromes