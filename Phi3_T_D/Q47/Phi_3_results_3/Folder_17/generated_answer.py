def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(22, 96 - (55 - 52)):
        for j in range(52, 56):
            substring = s[i:i + j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes