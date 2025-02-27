def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(len(s) - 4):
        for j in range(i + 3, i + 5):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes