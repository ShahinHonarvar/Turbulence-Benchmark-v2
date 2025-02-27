def palindromes_of_specific_lengths(string):
    substring = string[0:101]
    palindromes = set()
    for length in range(3, 16):
        for i in range(len(substring) - length + 1):
            substring = substring[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes