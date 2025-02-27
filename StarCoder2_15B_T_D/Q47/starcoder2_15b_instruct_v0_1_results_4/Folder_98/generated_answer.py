def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(21):
        for j in range(i + 5, 21):
            for k in range(i, j):
                substring = s[i:j + 1]
                if substring[k] == substring[j - k]:
                    palindromes.add(substring)
    return palindromes