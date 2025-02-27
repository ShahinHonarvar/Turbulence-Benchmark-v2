def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(len(string) - 9):
        substring = string[i:i + 10]
        for j in range(3, 6):
            for k in range(len(substring) - j + 1):
                window = substring[k:k + j]
                if window == window[::-1] and window.isalpha():
                    palindromes.add(window)
    return palindromes