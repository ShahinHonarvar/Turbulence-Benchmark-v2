def palindromes_of_specific_lengths(string):
    substring = string[16:78]
    palindromes = set()
    for length in range(43, 48):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes