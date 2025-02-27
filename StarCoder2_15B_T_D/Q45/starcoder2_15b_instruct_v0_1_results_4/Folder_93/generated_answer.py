def palindromes_between_indices(string):
    s = string.lower()
    palindromes = set()
    for i in range(2, 8):
        for j in range(i + 1, 8):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes