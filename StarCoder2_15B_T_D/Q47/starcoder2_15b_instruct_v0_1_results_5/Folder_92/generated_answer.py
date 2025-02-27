def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(len(string) - 4):
        substring = string[i:i + 5]
        for j in range(3, 5):
            for k in range(len(substring) - j + 1):
                window = substring[k:k + j]
                if window == window[::-1]:
                    if all((ch.isalpha() for ch in window)):
                        palindromes.add(window)
    return palindromes