def palindromes_between_indices(s):
    subset = s[7:10]
    subset = subset.lower()
    unique_chars = set(subset)
    palindromes = set()
    for char in unique_chars:
        for i in range(len(subset)):
            for j in range(i + 2, len(subset) + 1):
                substring = subset[i:j]
                if substring == substring[::-1] and len(substring) >= 3:
                    palindromes.add(substring)
    return palindromes