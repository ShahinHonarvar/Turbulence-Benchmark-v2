def palindromes_between_indices(s):
    subset = s[3:9]
    subset = subset.lower()
    letters = set(subset)
    result = set()
    for i in range(len(subset)):
        for j in range(i + 5, len(subset) + 1):
            sub = subset[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result