def palindromes_between_indices(s):
    subset = s[3:9]
    subset = subset.lower()
    subset = ''.join(sorted(subset))
    result = set()
    for i in range(len(subset)):
        for j in range(i + 6, len(subset) + 1):
            substring = subset[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result