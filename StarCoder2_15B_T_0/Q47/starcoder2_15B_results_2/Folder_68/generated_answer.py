def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(len(string) - 50):
        substring = string[i:i + 50]
        for j in range(50, 100):
            for k in range(len(substring) - j):
                window = substring[k:k + j]
                if window == window[::-1]:
                    palindromes.add(window)
    return palindromes