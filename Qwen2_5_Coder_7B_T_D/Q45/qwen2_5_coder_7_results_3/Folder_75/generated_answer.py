def palindromes_between_indices(s):
    subset = s[2:5].lower()
    palindromes = set()
    for i in range(len(subset)):
        for j in range(i + 3, len(subset) + 1):
            substring = subset[i:j]
            if substring == substring[::-1] and substring not in palindromes:
                palindromes.add(substring)
    return palindromes