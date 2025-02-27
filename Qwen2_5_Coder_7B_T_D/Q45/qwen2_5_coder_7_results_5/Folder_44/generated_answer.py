def palindromes_between_indices(s):
    subset = s[2:8].lower()
    palindromes = set()
    for i in range(len(subset)):
        for j in range(i + 2, len(subset) + 1):
            substring = subset[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes