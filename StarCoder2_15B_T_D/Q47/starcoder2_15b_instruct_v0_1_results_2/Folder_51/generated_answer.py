def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(3, 5):
        for i in range(2, len(string) - 8):
            substring = string[i:i + 8]
            for j in range(len(substring) - length + 1):
                window = substring[j:j + length]
                if window == window[::-1]:
                    palindromes.add(window)
    return palindromes